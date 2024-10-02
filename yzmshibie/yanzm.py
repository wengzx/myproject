import ddddocr # 导入 ddddocr
import requests
import json
import base64
from matplotlib.font_manager import json_load


code_url = "https://www.sssgame.com/api/member/getCaptcha?type=login&timestamp=1727693541838"  # 验证码图片地址
reponse = requests.get(url=code_url)  # 请求验证码

#把响应数据json化为字典
ss=json.loads(reponse.text)

# 获取验证码图片地址
img_code_url1=ss['data']["codeUrl"]
print(img_code_url1)

try:
    # 截取uri的data:image/png;base64后端的uri
    img_code_url=img_code_url1.split(",")[1]
    # 这个就是解析
    ss=base64.b64decode(img_code_url)
    print(ss)

except Exception as e:
        print(f"base64_to_img error:{e}")


# 将验证码保存本地
filename = "a8.png"  # 定义一个图片地址
file = open(filename, "wb")  # 以二进制打开一个文件
file.write(ss)  # 写入二进制文件
file.close()  # 关闭文件


ocr = ddddocr.DdddOcr(show_ad=False) # 实例化

with open('a8.png', 'rb') as f: # 打开图片

    img_bytes = f.read() # 读取图片
    res = ocr.classification(img_bytes) # 识别

    # 打印验证码
    print(res)