import discord
import asyncio
from GenshinAPIList import Distoken
from GenshinAPIList import DiscordID1
# import main
# from GenshinAPIListForGithub import token
print("a") 
print(__name__)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # user = client.fetch_user(DiscordID1)
    global SendUser
    SendUser = await client.fetch_user(DiscordID1)
    print(f'We have logged in as {client.user}')
    print("さくせす")
    print("sakusesuato")
    # await Send_resin_time("hello1")
# test  
    
async def OverOneHundredEighy(UntilTwoHundred):
    await SendUser.send(f"180を超しています！200に達するまで{UntilTwoHundred}分です。！")
    print("konnitha")
    # await client.close()
    
async def caveat():
    await SendUser.send("樹脂が溢れています！")

async def BootBot():
    await client.start(Distoken)
    
print("読み込み")
# asyncio.run(BootBot())
# client.start(Distoken)