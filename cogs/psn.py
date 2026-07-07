import discord
from discord.ext import commands
from psnawp_api import PSNAWP
from psnawp_api.core.psnawp_exceptions import PSNAWPException
from utils.constants import NPSSO_global as NPSSO
from utils.helpers import accountIDformat

psnawp = PSNAWP(NPSSO)

class psn(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot       
    @discord.slash_command(description="Get a users resign id for use with store account id command")
    async def psn(self, ctx: discord.ApplicationContext, psn_usrname: str) -> None: 
        await ctx.defer()
        try:
            foundusr = psnawp.user(online_id=psn_usrname)
        except PSNAWPException as exc:
            await ctx.respond(f"{psn_usrname} could not be found!")
            return
        
        accountID19 = foundusr.account_id
        userhexid = accountIDformat(accountID19)
        # some info for embed 
        usrProfile = foundusr.profile()
        #embed 
        embdisplay = discord.Embed(title=f"Account: {psn_usrname}",)
        embdisplay.set_thumbnail(url=usrProfile['avatars'][1]['url'])
        embdisplay.add_field(
            name="Resign ID (Mobile)",
            value=f"`{userhexid}`",
            inline=False,
            )
        embdisplay.add_field(
            name="Resign ID (Desktop)",
            value=f"```\n{userhexid}\n```",
            inline=False,
            )
        await ctx.respond(embed=embdisplay)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(psn(bot))