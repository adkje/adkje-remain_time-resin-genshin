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

    
async def OverOneHundredEighy(UntilTwoHundred):
    await SendUser.send(f"180を超しています！200に達するまで{UntilTwoHundred}分です。！")
    print("konnitha")
    # await client.close()
    
async def caveat():
    await SendUser.send("樹脂が溢れています！")

async def BootBot():
    print("あああああああああああああああああああああああ")
    await client.start(Distoken)

# async def once():
#     print("hayouha")
#     await asyncio.sleep(20)  # 10秒後にボットを終了
#     await client.close(Distoken)


#     print("end")

# def aslkdj():
#     client.run(Distoken)


# aslkdj()
# asyncio.run(once())

