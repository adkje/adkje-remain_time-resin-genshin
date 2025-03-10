import discord
import asyncio
from ClassGenshinAPI import User
from GenshinAPIList import token
from GenshinAPIList import DiscordID1
# from GenshinAPIListForGithub import token
print("a")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
# async def aiueo():
#     user = await client.fetch_user(DiscordID1)
#     await user.send("hello2")


async def on_ready():
    print(f'We have logged in as {client.user}')
    user = await client.fetch_user(DiscordID1)
    print("さくせす")
    await user.send("hello2")
    # await aiueo()
    await asyncio.run(User.hello())
    

client.run(token)