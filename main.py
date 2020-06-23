import random       

from discord.ext import commands

from utils.config import DISCORD_TOKEN


def main():
    # define our cogs, which we use to split up
    # event and command functionality across different files
    cogs = [
        'cogs.commands',
        'cogs.events'
    ]

    # initialize our Discord bot with a command prefix
    bot = commands.Bot(command_prefix='!')

    # iterate over and load any cog
    for cog in cogs:
        bot.load_extension(cog)

    # run our bot
    bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
