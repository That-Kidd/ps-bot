import asyncio
import discord
from discord.ext import commands, tasks

from utils.constants import (
    ABUSE_SAVE_ACCID_LIMIT, ABUSE_USER_ACCID_LIMIT, ABUSE_WINDOW_DAYS, ABUSE_LOG_CHANNEL_ID,
    logger, abuse_logger
)
from utils.embeds import Color, Embed_t
from utils.workspace import (
    write_resign_db, check_abuse_db, user_resign_summary_db, top_offenders_db, prune_abuse_db
)

PRUNE_INTERVAL_HOURS = 24
TOP_LIMIT = 10
HASH_DISPLAY_LEN = 16
# discord rejects an embed field over 1024 characters, and rejects the whole
# message with it, so everything variable length below gets truncated
FIELD_LIMIT = 1024
# safety valve, if discord is rate limiting or down these would otherwise pile up
MAX_PENDING_ALERTS = 50

def fmt_hash(save_hash: bytes | None) -> str:
    if save_hash is None:
        return "N/A"
    return save_hash.hex()[:HASH_DISPLAY_LEN]

def fit_field(parts: list[str], total: int, sep: str = ", ") -> str:
    """Join what fits in one embed field, noting whatever did not."""
    if not parts:
        return "N/A"

    out = ""
    shown = 0
    for part in parts:
        candidate = part if not out else out + sep + part
        # leave room for the suffix that reports what got cut
        if len(candidate) > FIELD_LIMIT - 32:
            break
        out = candidate
        shown += 1

    if shown == 0:
        return f"({total} entries, too long to show)"
    if shown < total:
        out += f"{sep}... and {total - shown} more"
    return out

def fmt_accids(accids: list[int], total: int) -> str:
    return fit_field([f"`{accid:016x}`" for accid in accids], total)

class Abuse(commands.Cog):
    """Flags resign patterns that look like save reselling.

    Monitoring only, it never blocks a resign and never blacklists anyone. Every
    failure in here is swallowed, a broken abuse db must not take down /resign.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.channel_broken = False # stop retrying a channel ID that does not work
        self.pending = set() # keeps alert tasks alive, they are garbage collected otherwise
        self.prune_task.start()

    def cog_unload(self) -> None:
        self.prune_task.cancel()
        for task in self.pending:
            task.cancel()

    @tasks.loop(hours=PRUNE_INTERVAL_HOURS)
    async def prune_task(self) -> None:
        try:
            deleted = await prune_abuse_db(ABUSE_WINDOW_DAYS)
            if deleted > 0:
                abuse_logger.info(f"Pruned {deleted} resign entries older than {ABUSE_WINDOW_DAYS} days.")
        except Exception as e:
            logger.error(f"Could not prune abuse database: {e}")

    @prune_task.before_loop
    async def before_prune(self) -> None:
        await self.bot.wait_until_ready()

    async def record(
              self,
              user: discord.User | discord.Member,
              ps_accountid: str,
              title_id: str | None,
              save_hash: bytes
            ) -> None:
        """Record a resigned savefile and alert if it trips a rule.

        Called by cogs/resign.py after the resign succeeded.
        """
        try:
            await write_resign_db(save_hash, user.id, ps_accountid, title_id)
            counts = await check_abuse_db(save_hash, user.id, ABUSE_WINDOW_DAYS)

            rules = []
            if counts.save_accid_count >= ABUSE_SAVE_ACCID_LIMIT:
                rules.append(
                    f"**Shared save** - this exact save has been resigned to "
                    f"{counts.save_accid_count} different account IDs (limit {ABUSE_SAVE_ACCID_LIMIT})."
                )
            if counts.user_accid_count >= ABUSE_USER_ACCID_LIMIT:
                rules.append(
                    f"**Account fan-out** - this user has resigned to "
                    f"{counts.user_accid_count} different account IDs (limit {ABUSE_USER_ACCID_LIMIT})."
                )

            if not rules:
                return

            emb = discord.Embed(
                title="Possible resign abuse",
                description="\n".join(rules),
                color=Color.YELLOW.value
            )
            emb.add_field(name="User", value=f"{user.mention} (`{user.id}`)", inline=False)
            emb.add_field(name="Title ID", value=title_id or "N/A", inline=True)
            emb.add_field(name="Save hash", value=f"`{fmt_hash(save_hash)}`", inline=True)
            emb.add_field(name="Window", value=f"{ABUSE_WINDOW_DAYS} days", inline=True)
            emb.add_field(
                name="Account IDs for this save",
                value=fmt_accids(counts.save_accids, counts.save_accid_count), inline=False
            )
            emb.add_field(
                name="Account IDs for this user",
                value=fmt_accids(counts.user_accids, counts.user_accid_count), inline=False
            )
            emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

            await self._report(
                emb,
                f"{user.name} ({user.id}) - save {fmt_hash(save_hash)} - "
                f"{counts.save_accid_count} accids on save, {counts.user_accid_count} accids on user"
            )
        except Exception as e:
            logger.error(f"Could not record resign for abuse detection: {e}")

    async def _report(self, emb: discord.Embed, log_line: str) -> None:
        """The single destination seam, change here to post somewhere else.

        The log write is what actually guarantees the alert is kept. Posting to
        discord is dispatched in the background, so that being rate limited slows
        down nobody's resign.
        """
        abuse_logger.info(log_line)

        if not ABUSE_LOG_CHANNEL_ID or self.channel_broken:
            return

        if len(self.pending) >= MAX_PENDING_ALERTS:
            # discord is backed up, the log already has the alert so drop the post
            logger.error(f"Dropping abuse alert post, {len(self.pending)} already queued.")
            return

        task = asyncio.create_task(self._post(emb))
        self.pending.add(task)
        task.add_done_callback(self.pending.discard)

    async def _post(self, emb: discord.Embed) -> None:
        try:
            channel = self.bot.get_channel(ABUSE_LOG_CHANNEL_ID)
            if channel is None:
                channel = await self.bot.fetch_channel(ABUSE_LOG_CHANNEL_ID)
            await channel.send(embed=emb)
        except (discord.NotFound, discord.Forbidden) as e:
            # a wrong ID or missing permissions will never fix itself, stop trying
            self.channel_broken = True
            logger.error(
                f"Disabling abuse alert posting, channel {ABUSE_LOG_CHANNEL_ID} is unusable: {e}. "
                "Alerts are still written to logs/ABUSE.log."
            )
        except discord.HTTPException as e:
            # rate limits and transient failures, the log still has the alert
            logger.error(f"Could not post abuse alert to channel {ABUSE_LOG_CHANNEL_ID}: {e}")

    abuse_group = discord.SlashCommandGroup("abuse")

    @abuse_group.command(description="Check a user's resign activity in the current window.")
    @commands.is_owner()
    async def check(self, ctx: discord.ApplicationContext, user: discord.Option(discord.User)) -> None:
        try:
            summary = await user_resign_summary_db(user.id, ABUSE_WINDOW_DAYS)
        except Exception as e:
            logger.error(f"Could not read abuse database: {e}")
            await ctx.respond("Could not read the abuse database.", ephemeral=True)
            return

        emb = discord.Embed(
            title=f"Resign activity: {user.name}",
            description=f"Last {ABUSE_WINDOW_DAYS} days.",
            color=Color.DEFAULT.value
        )
        emb.add_field(name="Distinct account IDs", value=f"{summary['accid_count']} (limit {ABUSE_USER_ACCID_LIMIT})", inline=True)
        emb.add_field(name="Saves resigned", value=summary["resign_count"], inline=True)
        emb.add_field(
            name="Most spread save",
            value=f"`{fmt_hash(summary['top_save_hash'])}` to {summary['top_save_accids']} account IDs",
            inline=False
        )
        emb.add_field(
            name="Title IDs",
            value=fit_field(summary["title_ids"], summary["title_count"]), inline=False
        )
        emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)
        await ctx.respond(embed=emb, ephemeral=True)

    @abuse_group.command(description="Busiest users and most reused saves in the current window.")
    @commands.is_owner()
    async def top(self, ctx: discord.ApplicationContext) -> None:
        try:
            data = await top_offenders_db(ABUSE_WINDOW_DAYS, TOP_LIMIT)
        except Exception as e:
            logger.error(f"Could not read abuse database: {e}")
            await ctx.respond("Could not read the abuse database.", ephemeral=True)
            return

        user_lines = [f"<@{uid}> (`{uid}`): {count} account IDs" for uid, count in data["users"]]
        save_lines = [f"`{fmt_hash(h)}`: {count} account IDs" for h, count in data["saves"]]
        users = fit_field(user_lines, len(user_lines), sep="\n")
        saves = fit_field(save_lines, len(save_lines), sep="\n")

        emb = discord.Embed(
            title="Resign leaderboard",
            description=f"Last {ABUSE_WINDOW_DAYS} days, top {TOP_LIMIT}.",
            color=Color.DEFAULT.value
        )
        emb.add_field(name=f"Users (limit {ABUSE_USER_ACCID_LIMIT})", value=users, inline=False)
        emb.add_field(name=f"Saves (limit {ABUSE_SAVE_ACCID_LIMIT})", value=saves, inline=False)
        emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)
        await ctx.respond(embed=emb, ephemeral=True)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Abuse(bot))
