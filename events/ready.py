from discord.ext import commands
from Logger import Logger
logger = Logger()


class ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"Logined as {self.bot.user}.")

async def setup(bot):
    await bot.add_cog(ready(bot))