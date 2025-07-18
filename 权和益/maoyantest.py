import requests
import json
import yagmail
import schedule
import time



class maoyan:

    # 测试购买特惠商品
    def tehuizhifu(self):

        tehuiurl="https://yp.3cuc.com/retail/shop/exchangeGoods/submit"

        header={
            "Content-Type":"application/json"
        }

        data={
            "pay_type": 3,
            "price": "3.0",
            "suid": "10322",
            "uid": "1000603",
            "goods_list": "[{\"goods_id\": \"1504\",\"num\":1}]",
            "token": "MzowOTZjUFFabUVoZVFpd1VIK1VwT1NXMy9YSDQvVld4UGs5TVFETWJxekdjM2NqbjZnZ1huOjE3MDcwMzIwMTE=",
            "code_id": "376",
            "encrypted_string": "TJQr+9PXC1KgUYfC/jcPqj4efJbL2SAe6UBG1MFX91iRUeVbOijWqIU1sPhFzNdK1hqz8o7eRFFZg+dgcTfEhTYBSg3vXG3/c5flDZUimB5fkzmGyV8a2zrn6C2REYRXF7/fRKdJwIolOwvR0NvBbEeY4toLwwdjdInAVSv1OvG19c49kCbuxGuKLWNuUsDni7PMPIs4POhdfKzpjdXqProrEHwH1m0BhajOGnIiUac0m4izhaCOfvhasu5/tJB5G5X72mD0bdmSMdY8AZIWHCisZNzF8609fszep5PSCfS+3hrw/HHARl0Yl7GBBdLvY8JMP0gL9Agev2Uwi7kVDw==",
            "check_pwd": "true",
            "device_id": "9D04307B-73D9-4A14-B578-0BCDCFAA61D2",
            "version": "2.5.3",
            "plat": "ios",
            "plat_ver": "16.3.1",
            "app_plat": "app",
            "app_ver": "1.0.0.2",
            "mobile_model": "iPhone",
            "client": "app",
            "getui_cid": "8b49a81a83d412e773f7b7ef5d3b95f5",
            "deviceToken": "c4e6f88b895f7e5fad207ace89cc767dd9885822406c96ab937ed70bc47cf571",
            "timestamp": 1705738159,
            "sign": "2cd76d94a7baf9359deb6d6ae6cfac3d"
        }

        re=requests.post(url=tehuiurl,headers=header,json=data).text

        res=json.loads(re)

        # print(res)

        if res["msg"]=="支付成功":
            print("支付成功，测试通过")
        else:
            print("支付失败，测试不通过")

    # 测试积分支付商品
    def jifenzhifu(self):
        jifenurl="https://yp.3cuc.com/retail/shop/VerificatePoints/verify_code"
        headers = {
            "Content-Type": "application/json"
        }
        data={
            "encrypted_string": "EmsDCIcGpl5zaN2bnUySE+R1m8qdy9LqWXohuBMrUmrbhUkkWUnZme7ngbBz076NXi08kLicfexNKU/2U74ANtcQbFbjT5zsEu5voPMD4K0W4P6VPQgFZ7tfyQhz3UNLk8F+A3eX6alQ83DKVd2npoUiSuq6fNgr1DlUMYiP9w6OdaQFp5a/YjWRQ991UpPLgbqeji0p7BmSYTTkoPli9jIYvE9g2VTWY+2hvoGXTgQ1mGMCFAsNDlQTtFQhAkb3LDTSjYDrKfWrpNJZifnypYULZmCh+e5eboqg/AUBCipln626ZUOJlGPH1rQUMUqTfNO86/64hB4WN62PyjOWhQ==",
            "check_pwd": "true",
            "device_id": "E1EDFE40-4518-49CC-AB13-B601089784A2",
            "suid": "10322",
            "goods_id": "1921",
            "num": 1,
            "token": "Mzo5ZTgyTytKVkpKa2VETFhLZTQ4elNybEdsRW5VdTRJN28wV0RtUWdUM3FPL2JaK2lxc2dEOjE3MDcxODQ4Mzg=",
            "version": "2.5.3",
            "plat": "ios",
            "plat_ver": "16.3.1",
            "app_plat": "app",
            "app_ver": "1.0.0.2",
            "mobile_model": "iPhone",

            "getui_cid": "8b49a81a83d412e773f7b7ef5d3b95f5",
            "deviceToken": "ae20c36ef5bbc6ede7cedb1b62eddb6e798ceebb004c23e5a72984a184636bd6",
            "timestamp": 1705889570,
            "sign": "19274b559ac613ed3f149be9ea26784c"
            }
        jifenres = requests.post(url=jifenurl, headers=headers, json=data).text

        # print(jifenres)
        res = json.loads(jifenres)
        # print(res["data"]["remark"])
        if res["data"]["remark"]=="成功兑换耳机":
            print("返回数据正确，测试通过")

        #

    # 发送邮件
    def sendemail(self):

        # 链接邮箱服务器  password授权码
        yag = yagmail.SMTP(user="1294424625@qq.com", password="dmaosvisrjzaibai", host='smtp.qq.com')

        # 邮箱正文
        contents = ['This is the body, and here is just text http://somedomain/image.png',
                    'You can find an audio file attached.', '/local/path/song.mp3']
        # 发送邮件
        yag.send('1294424625@qq.com', 'subject', contents)

if __name__ == '__main__':
    aa=maoyan()
    schedule.every().day.at("16:39").do(aa.tehuizhifu)
    # aa.tehuizhifu()
    # aa.jifenzhifu()
    while True:
        schedule.run_pending()
        time.sleep(1)