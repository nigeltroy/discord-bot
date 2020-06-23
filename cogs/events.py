import random

import discord
from discord.ext import commands

from utils.config import DISCORD_GUILD


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # triggers on connection and client ready
    @commands.Cog.listener()
    async def on_ready(self):
        # mostly for debugging
        print('Connected')

    # triggers on new member joining the guild
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # send a DM to any new member
        guild = discord.utils.get(self.bot.guilds, name=DISCORD_GUILD)
        await member.create_dm()
        await member.dm_channel.send(
            f"Hey, {member.name}, welcome to {guild}! "
            f"Please be respectful and nice!"
        )

        # randomly assign a role to a new member
        role_str = random.choice(["E-girls", "Simps"])
        role = discord.utils.get(guild.roles, name=role_str)
        await member.add_roles(role)


def setup(bot):
    bot.add_cog(EventCog(bot))
