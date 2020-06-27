import daemon
from discord.ext import commands

from utils.config import DISCORD_TOKEN


def main():
    # Define our cogs, which we use to split up
    # event and command functionality across different files
    cogs = [
        'cogs.commands',
        'cogs.events'
    ]

    # Initialize our Discord bot with a command prefix
    bot = commands.Bot(command_prefix='!')

    # Iterate over and load any cog
    for cog in cogs:
        bot.load_extension(cog)

    # Run our bot
    bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    # Daemonize the bot
    # with daemon.DaemonContext():
    main()
