import asyncio
import base64
import discord
import requests
from discord.ext import commands
from psnawp_api.core.psnawp_exceptions import (
    PSNAWPError, PSNAWPNotFoundError, PSNAWPAuthenticationError, PSNAWPUnauthorizedError, PSNAWPBadRequestError
)
from psnawp_api.utils.endpoints import BASE_PATH, API_PATH
from psnawp_api.utils.misc import extract_region_from_npid
from utils.constants import psnawp, NPSSO_global, logger, PSN_USERNAME_RE
from utils.orbis import handle_accid

NPSSO_ERROR_MSG = "PSN lookup is unavailable, the bot's NPSSO token is missing or expired."
EMOJIS = {
    "true": "<:true:1270542950501187614>",
    "false": "<:false:1397356242225201315>",
    "psplus": "<:psplus:1265158401709838356>",
    "plat": "<:plat:1265158280821346347>",
    "gold": "<:gold:1265158298781483071>",
    "silver": "<:silver:1265158313662746684>",
    "bronze": "<:bronze:1265158328884138006>",
    "levelmax": "<:levelmax:1265781813922631720>",
    "bronze1": "<:bronze1:1265785634287780016>",
    "bronze2": "<:bronze2:1265785655003320351>",
    "bronze3": "<:bronze3:1265785668492070953>",
    "silver1": "<:silver1:1265785727388749845>",
    "silver2": "<:silver2:1265785741766824129>",
    "silver3": "<:silver3:1265785754072907937>",
    "gold1": "<:gold1:1265785682232869098>",
    "gold2": "<:gold2:1265785695507578880>",
    "gold3": "<:gold3:1265785709386797056>",
}

def lookup_profile(username: str) -> dict:
    return psnawp.authenticator.get(
        url=f"{BASE_PATH['legacy_profile_uri']}{API_PATH['legacy_profile'].format(online_id=username)}",
        params={
            "fields": "accountId,onlineId,currentOnlineId,npId,avatarUrls,plus,aboutMe,trophySummary(@default,level,progress,earnedTrophies)",
            "avatarSizes": "xl",
        },
    ).json()["profile"]

def level_emoji(level: int) -> str:
    if level >= 999:
        return EMOJIS["levelmax"]
    tier = 9 if level >= 800 else level // 100 + 1
    metal = ("bronze", "silver", "gold")[(tier - 1) // 3]
    return EMOJIS[f"{metal}{(tier - 1) % 3 + 1}"]

def build_embed(profile: dict, username: str) -> discord.Embed:
    account_id = profile["accountId"]
    online_id = profile.get("currentOnlineId") or profile.get("onlineId") or username
    plus = EMOJIS["true"] if profile.get("plus") else EMOJIS["false"]

    embed = discord.Embed(
        title=f"{online_id} | {EMOJIS['psplus']} {plus}",
        description=profile.get("aboutMe") or "`-`",
        timestamp=discord.utils.utcnow(),
    )
    embed.set_author(
        name="Playstation Network",
        icon_url="https://media.discordapp.net/attachments/1381963775493668944/1567575566872215562/a6754f34a83ab5bf05912c513e7b0845.png?ex=6aecae03&is=6aeb5c83&hm=4acb7da6358c5a73d36c085700e4838811be1ae4251a1ec0e4f61c8e7fa39b4d&=&format=webp&quality=lossless",
    )
    embed.set_footer(text="Api Abuse v3.2")
    embed.set_image(url=f"https://image.api.playstation.com/profile/images/acct/prod/{account_id}/profile.JPEG")
    avatars = profile.get("avatarUrls")
    if avatars:
        embed.set_thumbnail(url=avatars[0]["avatarUrl"])

    region = extract_region_from_npid(profile.get("npId", ""))
    if region is not None:
        embed.add_field(name="Region", value=region.flag, inline=False)

    embed.add_field(name="Account ID", value=account_id)
    embed.add_field(name="Base64 ID", value=base64.b64encode(int(account_id).to_bytes(8, "little")).decode())
    resign_id = handle_accid(account_id)
    embed.add_field(name="Resign ID (Mobile)", value=f"`{resign_id}`", inline=False)
    embed.add_field(name="Resign ID (Desktop)", value=f"```\n{resign_id}\n```", inline=False)

    summary = profile.get("trophySummary", {})
    trophies = summary.get("earnedTrophies")
    if trophies:
        level = summary.get("level", 0)
        embed.add_field(name="Trophy Level", value=f"{level_emoji(level)} {level} | {summary.get('progress', 0)}%")
        embed.add_field(name="Platinum", value=f"{EMOJIS['plat']} {trophies.get('platinum', 0)}")
        embed.add_field(name="Gold", value=f"{EMOJIS['gold']} {trophies.get('gold', 0)}")
        embed.add_field(name="Trophy Count", value=str(sum(trophies.values())))
        embed.add_field(name="Silver", value=f"{EMOJIS['silver']} {trophies.get('silver', 0)}")
        embed.add_field(name="Bronze", value=f"{EMOJIS['bronze']} {trophies.get('bronze', 0)}")
    return embed


class PSN(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot       
    @discord.slash_command(description="Get a users resign id for use with store account id command")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def psn(self, ctx: discord.ApplicationContext, username: str) -> None: 
        if not 3 <= len(username) <= 16 or not PSN_USERNAME_RE.fullmatch(username):
            await ctx.respond("That isn't a valid PSN username. Usernames are 3-16 characters: letters, numbers, `-` and `_`.", ephemeral=True)
            return

        await ctx.defer()
        if not NPSSO_global.val:
            await ctx.respond(NPSSO_ERROR_MSG)
            return

        try:
            profile = await asyncio.to_thread(lookup_profile, username)
        except PSNAWPNotFoundError:
            await ctx.delete()
            await ctx.respond(f"{username} could not be found!", ephemeral=True)
            return
        except (PSNAWPAuthenticationError, PSNAWPUnauthorizedError, PSNAWPBadRequestError) as e:
            logger.exception(f"PSN authentication failed: {e}")
            await ctx.respond(NPSSO_ERROR_MSG)
            return
        except (PSNAWPError, requests.RequestException, KeyError) as e:
            logger.exception(f"PSN lookup failed: {e}")
            await ctx.respond("Couldn't reach PSN right now, try again later.")
            return

        await ctx.respond(embed=build_embed(profile, username))


def setup(bot: commands.Bot) -> None:
    bot.add_cog(PSN(bot))