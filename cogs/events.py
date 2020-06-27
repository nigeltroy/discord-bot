import random

import discord
from discord.ext import commands

from utils.config import DISCORD_GUILD, WELCOME_CHANNEL
from utils.welcome import get_welcome_message


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Triggers on connection and client ready
    @commands.Cog.listener()
    async def on_ready(self):
        # Mostly for debugging
        print('Connected')

    # Triggers on new member joining the guild
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = discord.utils.get(self.bot.guilds, name=DISCORD_GUILD)

        # Randomly assign a role to a new member
        role_str = random.choice(["E-girls", "Simps"])
        role = discord.utils.get(guild.roles, name=role_str)
        await member.add_roles(role)

        # Send a message to the #welcome channel
        welcome_channel = discord.utils.get(guild.channels, name=WELCOME_CHANNEL)
        singular_role_str = role_str[:-1] if role_str.lower().endswith('s') else role_str
        username = f"{singular_role_str.upper()} **{member.mention}**"
        await welcome_channel.send(
            get_welcome_message(username)
        )

    # Triggers on member leaving the guild
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = discord.utils.get(self.bot.guilds, name=DISCORD_GUILD)
        # Send a message to the #welcome channel
        welcome_channel = discord.utils.get(guild.channels, name=WELCOME_CHANNEL)
        await welcome_channel.send(
            f"**{str(member)}** has flown away to another world ~~"
        )


def setup(bot):
    bot.add_cog(EventCog(bot))
