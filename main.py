import asyncio
import requests
import time
import math
import GenshinAPIList as Glist
import GenshinDisco
# import GenshinAPIListForGithub as Glist

# url = "https://bbs-api.mihoyo.com/apihub/wapi/search"
# I don't know how to use the API with this URL.

# url = "https://api-os-takumi.hoyoverse.com/binding/api/getUserGameRolesByCookie"
# If you want other HoYoverse game as well as Genshin, this API provides less information than the URL below.

url = "https://bbs-api-os.hoyoverse.com/game_record/genshin/api/dailyNote"
# This URL provides the most information compared to the URLs above, but you must enter a UID of Genshin.

# Classを使う意味はありませんが直すのが面倒なので使ったまま！！
# APIの送信と待機時間の計算
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
        
    # 
    async def all_process(self):
        print("all_process")
        await asyncio.sleep(10)
        # クソみたいな実装方法だからいつか直す。多分。恐らく。
        while True:
            response = requests.get(url, cookies = self.cookies, params = self.params).json()
            self.resin_time = int(response["data"]["resin_recovery_time"])
            
            print(f"残り秒数は{self.resin_time}")

            self.wait_time = self.resin_time % 480
            #  次の樹脂までの秒数(60秒*8で八分)。sleep時間に使用。
            
            self.Max_minute = math.ceil(self.resin_time / 60)
            #   樹脂が200になるまでの分数。メッセージに載せる用。
            print(f"残り分数は{self.Max_minute}")
            

            if self.resin_time != 0:
                print(f"待つ秒数は{self.wait_time}")

                # if 100000 > self.resin_time:
                # デバッグ用

                if 9600 > self.resin_time:
                # 樹脂が180以上
                    print("mattemasu")
                    await GenshinDisco.OverOneHundredEighy(self.Max_minute)
                    await asyncio.sleep(self.wait_time)


            else:
                print(self.wait_time)
                # await GenshinDisco.caveat()
                await asyncio.sleep(1200)
                # 秘境の樹脂消費量に合わせた20樹脂(60*20)



User1 = User(0,"User1",Glist.User1_cookie_token,Glist.User1_ltoken,Glist.User1_ltuid,Glist.User1_uid)
# User2 = User(0,"User2",Glist.User1_cookie_token,Glist.User1_ltoken,Glist.User1_ltuid,Glist.User1_uid)

Alluser = [User1]  
async def AllBoot():
    await asyncio.gather(GenshinDisco.BootBot(),*(NowUser.all_process() for NowUser in Alluser))

asyncio.run(AllBoot())

