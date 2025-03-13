import discord
import asyncio
from GenshinAPIList import Distoken

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def second():
    while True:
        print("別の非同期処理を実行中…")
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print("Bot is ready!")
    # second()タスクを開始
    asyncio.create_task(second())

async def main():
    print("hello")
    # start()を使ってBotを実行し、終了後に次の処理を行う
    await client.start(Distoken)
    print("hello2")  # start()が終了するとここに戻ってきます

# 非同期のmain()関数を実行
asyncio.run(main())
