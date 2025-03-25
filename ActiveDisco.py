import discord
import asyncio
import BootBot
# import main
# from GenshinAPIListForGithub import token

print(f"{__name__}が読み込まれました。")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



async def OverOneHundredEighy(UntilTwoHundred,nowresin):
    await BootBot.SendUser.send(f"現在の樹脂は{nowresin}です！200に達するまで{UntilTwoHundred}分です！")

async def caveat():
    await BootBot.SendUser.send("樹脂が溢れています！")