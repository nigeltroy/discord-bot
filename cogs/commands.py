import discord
from discord.ext import commands

from utils.config import DISCORD_GUILD


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='msb', help="Gives an intro of this bot")
    async def intro(self, ctx):
        # on typing !megasimp, return a short intro
        guild = discord.utils.get(self.bot.guilds, name=DISCORD_GUILD)
        await ctx.send(
            f"Hi {ctx.author.mention}, I am {self.bot.user.name}, "
            f"a simple bot created by Nigel a.k.a vitasoyaddict. "
            f"I assign new members a random role: e-girl or simp. "
            f"I am also the biggest simp for {guild.owner.mention} <3"
        )


def setup(bot):
    bot.add_cog(CommandCog(bot))
