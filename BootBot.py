import discord
import asyncio
from GenshinAPIList import Distoken
from GenshinAPIList import DiscordID1

bot_ready = asyncio.Event()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # user = client.fetch_user(DiscordID1)
    global SendUser
    SendUser = await client.fetch_user(DiscordID1)
    print(f'We have logged in as {client.user}')
    bot_ready.set()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith('$getresin'):
    #     # await BootBot.SendUser.message.send(f"現在の樹脂は{main.nowresin}です！200に達するまで{main.UntilTwoHundred}分です！")
    #     await message.channel.send("現在の樹脂はaiueoです！200に達するまでaiueo分です！")

    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')

async def BootBot():
    await client.start(Distoken)