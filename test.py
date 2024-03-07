

import  requests
import json

for i in range(1,3):
    print(i)
data={
    "shop_sub_id": "10325",
    "token": "Mzo4Yzk3Z25sUmNqR0YxRWRmV2ZKa2ovU1J0K0QzTnd0TytncmFZb3IrbEZWNU5QS1ZrTFJqOjE3MDczMDA4ODM=",
    "version": "2.5.3",
    "plat": "ios",
    "plat_ver": "16.3.1",
    "app_plat": "app",
    "app_ver": "1.0.0.2",
    "mobile_model": "iPhone",
    "client": "app",
    "device_id": "D5B307AD-D872-4742-AE54-BA5522371243",
    "getui_cid": "8b49a81a83d412e773f7b7ef5d3b95f5",
    "deviceToken": "0bef849d3883703dfb3b21f608531ca98f2072051dc737b0b83a86daf05483e6",
    "timestamp": 1706005404,
    "sign": "e5618c374704e587476f5c8ec313fa87"
}

RES=requests.post(url="https://yp.3cuc.com/retail/verification/Arriveshop/cmt_point",headers={"Content-Type": "application/json"},json=data)
print(data)
res = RES.json()
print(res)