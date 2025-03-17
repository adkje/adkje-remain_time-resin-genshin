import Discord
from GenshinAPIList import Distoken
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
def on_ready():

  client.user.send("hello"):


client.run(Distoken)
