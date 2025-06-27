import requests
import json


#  执行登录操作
url="http://retail-shop.3cuc.com/userpage/login_user"

headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",}

 # 请求参数
datass={"loginnum":"13480823186",
    "password":"123123",
    "action":"password"}

# 直接请求返回结果
re=requests.post(url=url,headers=headers,data=datass)

# 获取cookie  第一中
print(re.headers.get("set-cookie").split(";")[0])

cookie=re.headers.get("set-cookie").split(";")[0]



# 设置公共请求头
headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
         "Cookie":cookie
         }

# 登录请求参数
logindata={
    "suid":"10323"
}

#请求登录接口
login=requests.post(url="http://retail-shop.3cuc.com/userpage/shop_sess",headers=headers,data=logindata)
print(login.text)

reslogin=login.json()

# 解析json
print(login.json())
if reslogin['msg']=="登录成功":
    #打印语句
    print("登录成功")


postdata={
    "page": 1,
    "limit": 15}
ss=requests.post(url="http://retail-shop.3cuc.com/stockmanage/getGoodsData",data=postdata,headers=headers).text
print(ss)
# posturllist = ["http://retail-shop.3cuc.com/stockmanage/getGoodsData",
#                "http://retail-shop.3cuc.com/stockmanage/getMaterialData",
#                "http://retail-shop.3cuc.com/stockmanage/getAccessoryData",
#                 "http://retail-shop.3cuc.com/stockmanage/getInventoryData",
#                "http://retail-shop.3cuc.com/stockmanage/getWarehousingData",
#                "http://retail-shop.3cuc.com/stockmanage/getOutboundGoodsData",
#                "http://retail-shop.3cuc.com/stockmanage/getSalesReportData",
#                ]
#
#
#
# for posturl in posturllist:
#     re=requests.post(url=posturl,data=postdata,headers=headers).text
#     print(re)
    # postres=json.loads(re)
    # if postres['code']==0:
    #     print("接口请求成功")
    # else:
    #     print("接口请求失败")
