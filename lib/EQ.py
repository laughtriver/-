from discord.ext import tasks, commands
import requests
import asyncio

p2pquake_url = "https://api.p2pquake.net/v2/history?codes=551&limit=1"


class EQcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=30)
    async def printer(self):
        p2pquake_json = requests.get(p2pquake_url).json()
        new_Eq_time = p2pquake_json[0]["earthquake"]["time"]
        new_Eq_lever = p2pquake_json[0]["earthquake"]["hypocenter"]["magnitude"]
        new_Eq_name = p2pquake_json[0]["earthquake"]["hypocenter"]["name"]
        if new_Eq_lever > 3.0:
            asyncio.run(self.notify_earthquake(new_Eq_time, new_Eq_name, new_Eq_lever))
    
    async def notify_earthquake(new_Eq_time, new_Eq_name, new_Eq_level):
        # await channel.send(f"{new_Eq_time}に地震が発生しました! {new_Eq_name} - マグニチュード {new_Eq_level}")
        pass


async def setup(bot):
    await bot.add_cog(EQcog(bot))
