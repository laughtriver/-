import discord
from discord.ext import commands
import requests
import asyncio
import os

intents = discord.Intents.default()
intents.typing = False
bot = commands.Bot(command_prefix=" ", intents=intents)


async def check_earthquake():
    while True:
        await asyncio.sleep(60)

p2pquake_url = "https://api.p2pquake.net/v2/history?codes=551&limit=1"

p2pquake_json = requests.get(p2pquake_url).json()
new_Eq_time = p2pquake_json[0]["earthquake"]["time"]
new_Eq_lever = p2pquake_json[0]["earthquake"]["hypocenter"]["magnitude"]
new_Eq_name = p2pquake_json[0]["earthquake"]["hypocenter"]["name"]


async def notify_earthquake(new_Eq_time, new_eq_name, new_eq_level):
    await channel.send(f"{new_Eq_time}に地震が発生しました! {new_Eq_name} - マグニチュード {new_Eq_lever}")

if new_Eq_lever > 3.0:
    asyncio.run(notify_earthquake(new_Eq_time, new_Eq_name, new_Eq_lever))


@bot.event
async def on_message(message):
    if 'earthquake' in message.content.lower():
        await notify_earthquake(new_Eq_time, new_Eq_name, new_Eq_lever)


async def main():
    await bot.start(os.getenv("DISCORD_TOKEN"))

    await check_earthquake()

if __name__ == "__main__":
    asyncio.run(main())

bot.run(os.getenv("DISCORD_TOKEN"))
