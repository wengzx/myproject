import requests
import json
import pandas as pd

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

# cookie 字典键值对
print(re.cookies.get_dict())

# cookie  键值字符串
print(re.cookies.get_dict()['3CUCSID'])

# 公共请求头
headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
         "Cookie":cookie
         }

# 登录请求参数
logindata={
    "suid":"10323"
}

#登录
login=requests.post(url="http://retail-shop.3cuc.com/userpage/shop_sess",headers=headers,data=logindata)
print(login.text)

reslogin=login.json()

# 解析json
print(login.json())
if reslogin['msg']=="登录成功":
    #打印语句
    print("登录成功")


# get请求

geturllist=["http://retail-shop.3cuc.com/retailgoods/getList?page=1&limit=15&goods_id=3072",
        "http://retail-shop.3cuc.com/cashierorder/order_data_new?page=1&limit=15",
        "http://retail-shop.3cuc.com/chainstore/getStoreList?page=1&limit=10",
       ]



for geturl in geturllist:
    re=requests.get(url=geturl,headers=headers).text

    # 将json字符转为python可识别对象
    res=json.loads(re)
    # print(json.loads(re))
    # print(json.loads(re.text))
    # getres=re.json()
    # 判断断言是否请求成功
    if res["code"]==0:
        print("接口请求成功")
    else:
        print("接口请求失败")


#post请求
posturllist = ["http://retail-shop.3cuc.com/stockmanage/getGoodsData",
               "http://retail-shop.3cuc.com/stockmanage/getMaterialData",
               "http://retail-shop.3cuc.com/stockmanage/getAccessoryData",
                "http://retail-shop.3cuc.com/stockmanage/getInventoryData",
               "http://retail-shop.3cuc.com/stockmanage/getWarehousingData",
               "http://retail-shop.3cuc.com/stockmanage/getOutboundGoodsData",
               "http://retail-shop.3cuc.com/stockmanage/getSalesReportData",
               ]

postdata={
    "page": 1,
    "limit": 15}

for posturl in posturllist:
    re=requests.post(url=posturl,data=postdata,headers=headers).text
    print(re)
    postres=json.loads(re)
    if postres['code']==0:
        print("接口请求成功")
    else:
        print("接口请求失败")

# 选择登录，门店




#
# re=requests.get(url)
#
# print(re.text)

# 请求头
# headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#          "Cookie":"3CUCSID=a01f9bad2ea9628f4bcf497fd8a600ab"
#          }
#
# # 请求参数
# datass={"loginnum":"13480823186",
#     "password":"123123",
#     "action":"password"}
#
# # res=requests.post(url=url1,data=datass,headers=headers)
# # print(res.json())
#
#
#
#
# spres=requests.get("http://retail-shop.3cuc.com/retailgoods/getList?page=1&limit=15&goods_id=3072")
#
#
# # 获取cookie并代入变量
# tycookie=spres.headers.get("set-cookie").split(";")[0]
# print(tycookie)








