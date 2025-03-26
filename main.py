import discord
import asyncio

import SendAPI
import BootBot

print(f"{__name__}が読み込まれました。")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# おまじない

async def OverOneHundredEighy(nowresin,UntilTwoHundred):
    await BootBot.SendUser.send(f"現在の樹脂は{nowresin}です。200に達するまで{UntilTwoHundred}分です！")

async def caveat():
    await BootBot.SendUser.send("樹脂が溢れています！")



async def while_process(NowNowUser):
        await BootBot.bot_ready.wait()
        while True:
            APIconsequence = await NowNowUser.Send_API()
            kekka = await NowNowUser.various_calculation(*(APIconsequence))

            # if 70000 > keisan_resin_time > 9120:
            # デバック用
            # if 9600 > kekka[0] > 9120:
            if 9600 > kekka[0] > 9100:
            # 樹脂が180以上181以下
                print(f"樹脂がmaxになるまで残り{kekka[1]}")
                await OverOneHundredEighy(kekka[3],kekka[1])
            
            await NowNowUser.Sleep_process(*(kekka))


async def aiueo():
    await asyncio.gather(BootBot.BootBot(),*(while_process(NowUser) for NowUser in SendAPI.Alluser))

asyncio.run(aiueo())