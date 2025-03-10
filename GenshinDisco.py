import discord
from GenshinAPIList import token
import GenshinAPIListForGithub
# 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
async def sendresin(message):
    await message.channnel.send('樹脂が200です。')
    

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(token)
