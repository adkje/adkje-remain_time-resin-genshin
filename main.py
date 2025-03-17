import asyncio
import requests
import time
import math
import GenshinAPIList as Glist
import ActiveDisco
# import GenshinAPIListForGithub as Glist

# url = "https://bbs-api.mihoyo.com/apihub/wapi/search"
# I don't know how to use the API with this URL.

# url = "https://api-os-takumi.hoyoverse.com/binding/api/getUserGameRolesByCookie"
# If you want other HoYoverse game as well as Genshin, this API provides less information than the URL below.

url = "https://bbs-api-os.hoyoverse.com/game_record/genshin/api/dailyNote"
# This URL provides the most information compared to the URLs above, but you must enter a UID of Genshin.

# これclassを使う意味ある？
# APIの送信
class User:
    # APIに必要な情報の格納
    def __init__(self,wait_time,name,cookie_token,ltoken,ltuid,uid):
        self.wait_time = wait_time
        self.name = name

        self.cookie_token = cookie_token
        self.ltoken = ltoken
        self.ltuid = ltuid
        self.uid = uid
        self.cookies = {
                          "ltoken_v2": self.ltoken,
                          "ltuid_v2": self.ltuid,
                          "cookie_token_v2": self.cookie_token,
                         }
      
        self.params =  {
                          "role_id": f"{self.uid}",
                          "server": 'os_asia',
                          "schedule_type": 1,
                        }
        
    # 違う処理を作るにあたってAPI送信=計算となるのは良くないと感じた。
    async def Send_API(self):
        print("SendAPI")
        self.Receive_response = requests.get(url, cookies = self.cookies, params = self.params).json()
        self.Receive_resin_time = int(self.Receive_response["data"]["resin_recovery_time"])
        return self.Receive_resin_time

async def keisan(keisan_resin_time):
    global keisan_wait_time
    keisan_wait_time = keisan_resin_time % 480
    #  次の樹脂までの秒数(60秒*8で八分)。sleep時間に使用。
    print(f"待つ秒数は{keisan_wait_time}")

    global Max_minute
    Max_minute = math.ceil(keisan_resin_time / 60)
    #   樹脂が200になるまでの分数。メッセージに載せる用。
    print(f"残り分数は{Max_minute}")
    
    return keisan_resin_time,Max_minute,keisan_wait_time
    
    

async def okurimasu(keisan_resin_time,Max_minute,keisan_wait_time):
    if keisan_resin_time != 0:
    # if 100000 > self.resin_time:
    # デバッグ用
        print("okurimasu")

        if 9600 > keisan_resin_time:
        # 樹脂が180以上
            print("mattemasu")
            await ActiveDisco.OverOneHundredEighy(Max_minute)
            await asyncio.sleep(keisan_wait_time)

    else:
        print(keisan_wait_time)
        await ActiveDisco.caveat()
        await asyncio.sleep(1200)
        # 秘境の樹脂消費量に合わせた20樹脂(60*20)


User1 = User(0,"User1",Glist.User1_cookie_token,Glist.User1_ltoken,Glist.User1_ltuid,Glist.User1_uid)
# User2 = User(0,"User2",Glist.User1_cookie_token,Glist.User1_ltoken,Glist.User1_ltuid,Glist.User1_uid)

Alluser = [User1]

# async fdef handle_user(user):
#     ohayou = await user.Send_API()
#     naze = await keisan(ohayou)
#     await okurimasu(naze)

# async def aiueo():
#     # すべてのユーザーを同時に処理するためにgatherを使用
#     await asyncio.gather(*(handle_user(user) for user in Alluser))

# async def main():
#     # ボットとユーザー処理を同時に実行
#     await asyncio.gather(
#         ActiveDisco.BootBot(),
#         aiueo()
#     )

# # # メインコルーチンを開始
# asyncio.run(main())

async def aiueo(ohayou):
        ohayou = await ohayou.Send_API()
        naze =  await keisan(ohayou)
        await okurimasu(*(naze))

async def konnnitiha():
        await asyncio.gather(aiueo(ohayou) for ohayou in Alluser)
        
async def main():
    # await asyncio.gather(ActiveDisco.BootBot(),*(aiueo(NowUser) for NowUser in Alluser))
    await asyncio.gather(ActiveDisco.BootBot(),konnnitiha())

asyncio.run(main())
