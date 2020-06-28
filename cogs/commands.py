import time

import discord
from discord.ext import commands

from utils.config import DISCORD_GUILD


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # On typing !megasimpbot, return a short intro
    @commands.command(name='megasimpbot', help="Gives an intro of this bot")
    async def intro(self, ctx):
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

    # On typing !owo, return a meme
    @commands.is_nsfw()
    @commands.command(name='owo', help="What's this?")
    async def owo(self, ctx):
        await ctx.send("What's this?")
        time.sleep(2)
        for _ in range(4):
            await ctx.send(".")
            time.sleep(2)
        await ctx.send(
            f"Rawr x3 nuzzles how are you **{ctx.author.name}** pounces on you "
            f"**{ctx.author.name}** you're so warm o3o notices **{ctx.author.name}** have a bulge o: "
            f"someone's happy ;) nuzzles **{ctx.author.name}'s** necky wecky~ murr~ "
            f"hehehe rubbies **{ctx.author.name}'s** bulgy wolgy **{ctx.author.name}** you're so big :oooo "
            f"rubbies more on **{ctx.author.name}'s** bulgy wolgy it doesn't stop growing "
            f"·///· kisses **{ctx.author.name}** and lickies **{ctx.author.name}'s** necky daddy likies (; "
            f"nuzzles wuzzles I hope daddy really likes $: wiggles butt "
            f"and squirms I want to see **{ctx.author.name}'s** big daddy meat~ "
            f"wiggles butt I have a little itch o3o wags tail "
            f"can you please get my itch~ puts paws on **{ctx.author.name}'s** chest nyea~ "
            f"its a seven inch itch rubs **{ctx.author.name}'s** chest can you help me pwease "
            f"squirms pwetty pwease sad face I need to be punished "
            f"runs paws down **{ctx.author.name}'s** chest and bites lip like "
            f"I need to be punished really good~ paws on **{ctx.author.name}'s** bulge "
            f"as I lick my lips I'm getting thirsty. I can go for "
            f"some milk unbuttons **{ctx.author.name}'s** pants as my eyes glow "
            f"you smell so musky :v licks shaft mmmm~ so musky "
            f"drools all over **{ctx.author.name}'s** cock **{ctx.author.name}'s** daddy meat I like fondles "
            f"Mr. Fuzzy Balls hehe puts snout on balls and inhales deeply "
            f"oh god im so hard~ licks balls punish me daddy~ nyea~ squirms more "
            f"and wiggles butt I love **{ctx.author.name}'s** musky goodness bites lip "
            f"please punish me licks lips nyea~ suckles on **{ctx.author.name}'s** tip so good "
            f"licks pre of **{ctx.author.name}'s** cock salty goodness~ eyes role back "
            f"and goes balls deep mmmm~ moans and suckles"
        )

    # On typing !dorime, play the OG dorime doge video
    @commands.command(name='dorime', help="Interimo Adapare Dorime")
    async def dorime(self, ctx):
        url = "https://www.youtube.com/watch?v=kLaaJ_aeoyM"
        await ctx.send(url)

    # On typing !hydrate, play the moist garfield video
    @commands.command(name='hydrate', help="OH DEARRRRRRRR")
    async def hydrate(self, ctx):
        url = "https://www.youtube.com/watch?v=7zPfj5_Y0uY"
        await ctx.send(url)


def setup(bot):
    bot.add_cog(CommandCog(bot))
