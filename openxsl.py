import pdb

import testxl
import requests
import json
import yagmail
# bk=openpyxl.load_workbook(r"C:\Users\Thinkpad\Desktop\88x.xlsx")
#
# # sheet1=bk.get_sheet_name('Sheet1')
# sheet=bk.active

# minrow=sheet.min_row #最小行、
# maxrow=sheet.max_row
# mincol=sheet.min_column #最小列
# maxcol=sheet.max_column #最大列
#
# # 读取数据
# aa=sheet.cell(row=2,column=2).value
# print(aa)


class ceshi():
    bb = []
    cookie=""
    # 设置公共请求头
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Cookie": cookie
               }
    def login(self):
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

        ceshi.cookie=re.headers.get("set-cookie").split(";")[0]

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



    def  apitest(self):

        #  执行登录操作
        url = "http://retail-shop.3cuc.com/userpage/login_user"

        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", }

        # 请求参数
        datass = {"loginnum": "13480823186",
                  "password": "123123",
                  "action": "password"}

        # 直接请求返回结果
        re = requests.post(url=url, headers=headers, data=datass)

        # 获取cookie  第一中
        print(re.headers.get("set-cookie").split(";")[0])

        cookie = re.headers.get("set-cookie").split(";")[0]

        headers["cookie"] = cookie

        # 登录请求参数
        logindata = {
            "suid": "10323"
        }

        # 请求登录接口
        login = requests.post(url="http://retail-shop.3cuc.com/userpage/shop_sess", headers=headers, data=logindata)
        print(login.text)

        reslogin = login.json()

        # 解析json
        print(login.json())
        if reslogin['msg'] == "登录成功":
            # 打印语句
            print("登录成功")


        # 写入数据
        geturllist=["http://retail-shop.3cuc.com/retailgoods/getList?page=1&limit=15&goods_id=3072",
            "http://retail-shop.3cuc.com/cashierorder/order_data_new?page=1&limit=15",
            "http://retail-shop.3cuc.com/chainstore/getStoreList?page=1&limit=10",
           ]
        print(cookie)
        for url in geturllist:
            req=requests.get(url=url,headers=headers).text
            print(req)
            res = json.loads(req)

            aa=[]

            aa.append(url)
            if res["code"] == 0:

                print("接口请求成功")
                getmethod="get"
                duanyan ="pass"
                aa.append(getmethod)
                aa.append(duanyan)
                ceshi.bb.append(aa)

            else:
                print("接口请求成功")
                getmethod = "get"
                duanyan ="error"
                aa.append(getmethod)
                aa.append(duanyan)

                ceshi.bb.append(aa)


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
            # print(posturl)
            # print(postdata)
            print(headers)
            re=requests.post(url=posturl,data=postdata,headers=headers).text
            print(re)

            postres=json.loads(re)


            aa=[]

            aa.append(posturl)
            if res["code"] == 0:

                print("接口请求成功")
                postmethod = "post"

                duanyan ="pass"
                aa.append(postmethod)
                aa.append(duanyan)
                ceshi.bb.append(aa)

            else:
                print("接口请求成功")
                postmethod = "post"
                duanyan ="error"
                aa.append(postmethod)
                aa.append(duanyan)
                ceshi.bb.append(aa)


    def createxcel(self):
        # 表对象
        bk = testxl.Workbook()
        sheet = bk.active

        # 设置表头
        sheet['A1'] = "接口"
        sheet['B1'] = "请求方式"
        sheet['C1'] = "是否通过"


    #     保存文件
        for i in range(len(ceshi.bb)):
            sheet.append(ceshi.bb[i])
        bk.save(r'C:\Users\Thinkpad\Desktop\userinfo.xlsx')


# 发送邮件
    def sendemail(self):
        #链接邮箱服务器  password授权码
        yag = yagmail.SMTP( user="1294424625@qq.com", password="dmaosvisrjzaibai", host='smtp.qq.com')

        # 邮箱正文
        contents = ['This is the body, and here is just text http://somedomain/image.png',
                    'You can find an audio file attached.', '/local/path/song.mp3']

        # 发送邮件
        yag.send('1294424625@qq.com', 'subject', contents)


        # 发送带附件的邮件
        yag.send('1294424625@qq.com', 'subject', contents,["C://Users/Thinkpad/Desktop/userinfo.xlsx"])

if __name__ == '__main__':
    aa=ceshi()
    # aa.login()
    aa.apitest()
    aa.createxcel()