import logging
from Logger import Logger
import discord
from discord.ext import commands
import settings

cogs = ["events.ready","lib.EQ"]

logger = Logger()
logger.remove_oldlog()
logger._create_log_gitignore()
logger.info("Start main.py")

class EQ_Bot(commands.Bot):
    """
    Discord.pyのBot定義ポイントです。
    """

    def __init__(self):
        super().__init__(
            command_prefix="s!",
            intents=discord.Intents.all(),
            application_id=settings.DISCORD_APP_ID
        )
        self.version = "1.0.0-beta"
        self.admin_user: list[int] = settings.ADMIN_USER

    async def setup_hook(self) -> None:
        for cog in cogs:
            await self.load_extension(cog)
            logger.info("Loaded "+cog)

        await bot.tree.sync(
            guild=discord.Object(id=int(settings.GUILD_ID)))


bot = EQ_Bot()
bot.run(settings.DISCORD_TOKEN)
