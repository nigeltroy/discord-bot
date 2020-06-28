from sys import exc_info

from discord.ext import commands

from utils.logger import logger


class ErrorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Triggers on any event exception raised
    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        logger.error(
            f"**EVENT ERROR**\n"
            f"Args: {args}\n"
            f"Kwargs: {kwargs}\n"
            f"Event: {event}\n"
            f"{exc_info()}"
        )

    # Triggers on any command exception raised
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logger.error(
            f"**COMMAND ERROR**\n"
            f"User: {ctx.author}\n"
            f"{error}"
        )


def setup(bot):
    bot.add_cog(ErrorCog(bot))
