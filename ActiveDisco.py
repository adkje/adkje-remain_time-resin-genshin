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
bot_ready = asyncio.Event()

@client.event
async def on_ready():
    print("aiueo")
    # user = client.fetch_user(DiscordID1)
    global SendUser
    SendUser = await client.fetch_user(DiscordID1)
    print(f'We have logged in as {client.user}')
    print("さくせす")
    bot_ready.set()

    
async def OverOneHundredEighy(UntilTwoHundred):
    await SendUser.send(f"180を超しています！200に達するまで{UntilTwoHundred}分です。！")
    print("konnitha")
    # await client.close()

async def prepare_bot():
    print("あああああああああああああああああああああああ")
    
    # バックグラウンドでボットを起動する
    bot_task = asyncio.create_task(client.start(Distoken))
    
    # ボットが準備できるまで待機（タイムアウト付き）
    try:
        await asyncio.wait_for(bot_ready.wait(), timeout=30)
        print("ボット準備完了")
        return True
    except asyncio.TimeoutError:
        print("ボット準備タイムアウト")
        return False

print("githubのtest")

async def caveat():
    await SendUser.send("樹脂が溢れています！")

# async def BootBot():
#     print("あああああああああああああああああああああああ")
#     await client.start(Distoken)
#     print("iiiiiiiiiiii")

# async def once():
#     print("hayouha")
#     await asyncio.sleep(20)  # 10秒後にボットを終了
#     await client.close(Distoken)


#     print("end")

# def aslkdj():
#     client.run(Distoken)


# aslkdj()
# asyncio.run(once())