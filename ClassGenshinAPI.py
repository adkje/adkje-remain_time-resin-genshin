import asyncio
import requests
import time
import GenshinDisco
import GenshinAPIList as Glist
import GenshinAPIListForGithub as Glist

# url = "https://bbs-api.mihoyo.com/apihub/wapi/search"
# I don't know how to use the API with this URL.

# url = "https://api-os-takumi.hoyoverse.com/binding/api/getUserGameRolesByCookie"
# If you want other HoYoverse game as well as Genshin, this API provides less information than the URL below.

url = "https://bbs-api-os.hoyoverse.com/game_record/genshin/api/dailyNote"
# This URL provides the most information compared to the URLs above, but you must enter a UID of Genshin.



class User:
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

    async def all_process(self):
        while True:
            response = requests.get(url, cookies = self.cookies, params = self.params).json()
            self.resin_time = int(response["data"]["resin_recovery_time"])
            print(self.resin_time)
            self.wait_time = self.resin_time % 480
            #  次の樹脂までの時間(60秒*8で八分)

            if self.wait_time != 0:
                print(self.wait_time)
                await asyncio.sleep(self.wait_time)

            elif 601 > self.resin_time:
                print(self.wait_time)
                await asyncio.sleep(self.wait_time)

            else:
                print(self.wait_time)
                await asyncio.sleep(1200)
                # 秘境の樹脂消費量に合わせた20樹脂(60*20)

    async def hello():
        await asyncio.gather(*(NowUser.all_process() for NowUser in Alluser))

User1 = User(0,"User1",Glist.User1_cookie_token,Glist.User1_ltoken,Glist.User1_ltuid,Glist.User1_uid)
# User2 = User(0,"User2",Glist.User1_cookie_token,Glist.User1_ltoken,Glist.User1_ltuid,Glist.User1_uid) 

Alluser = [User1]

asyncio.run(User.hello())

# 多分計算部分とsleep部分はこれで完成かな？