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

async def once():
    global count
    if count == 0:
        await client.close()
        count = count + 1
        print(count)

count = 0

@client.event
async def on_ready():
    # user = client.fetch_user(DiscordID1)
    global SendUser
    SendUser = await client.fetch_user(DiscordID1)
    print(f'We have logged in as {client.user}')
    print("さくせす")
    # await once()

    
async def OverOneHundredEighy(UntilTwoHundred):
    await SendUser.send(f"180を超しています！200に達するまで{UntilTwoHundred}分です。！")
    print("konnitha")
    # await client.close()
    
async def caveat():
    await SendUser.send("樹脂が溢れています！")

async def BootBot():
    await client.start(Distoken)

# client.run(Distoken)
print("読み込み")
