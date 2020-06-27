import time

import discord
from discord.ext import commands

from utils.config import DISCORD_GUILD


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='megasimpbot', help="Gives an intro of this bot")
    async def intro(self, ctx):
        # On typing !megasimp, return a short intro
        guild = discord.utils.get(self.bot.guilds, name=DISCORD_GUILD)
        bot_info = await self.bot.application_info()
        member_converter = commands.MemberConverter()
        owner_as_member = await member_converter.convert(ctx, bot_info.owner.name)
        await ctx.send(
            f"Hi {ctx.author.mention}, I am {self.bot.user.name}, "
            f"a simple bot created by {bot_info.owner.name} "
            f"a.k.a {owner_as_member.nick}. "
            f"I assign new members a random role: e-girl or simp. "
            f"I am also the biggest simp for "
            f"{guild.owner.top_role.name} {guild.owner.display_name} <3"
        )

    @commands.command(name='owo', help="What's this?")
    async def owo(self, ctx):
        # On typing !owo, return a meme
        await ctx.send("What's this?")
        time.sleep(2)
        for _ in range(5):
            await ctx.send(".")
            time.sleep(2)
        img = 'owo.jpg'
        file = discord.File(f"assets/{img}", filename=img)
        await ctx.send(file=file)

    @commands.command(name='dorime', help="Interimo Adapare Dorime")
    async def dorime(self, ctx):
        # On typing !dorime, play the OG dorime doge video
        url = "https://www.youtube.com/watch?v=kLaaJ_aeoyM"
        await ctx.send(url)
        
    @commands.command(name='hydrate', help="OH DEARRRRRRRR")
    async def hydrate(self, ctx):
        # On typing !hydrate, play the moist garfield video
        url = "https://www.youtube.com/watch?v=7zPfj5_Y0uY"
        await ctx.send(url)


def setup(bot):
    bot.add_cog(CommandCog(bot))
