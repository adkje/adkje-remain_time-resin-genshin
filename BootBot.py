import discord
import asyncio


from PassiveDisco import aiueo
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
    await aiueo(client,message)
    
async def BootBot():
    await client.start(Distoken)