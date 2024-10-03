
import streamlit as st
import ddddocr
import json

import  requests
from sympy.logic.algorithms.dpll import pl_true_int_repr

# 设置标题
st.title('在线验证码识别')

# 上传图片并展示
# uploaded_file = st.file_uploader("上传一张图片", type="png")

# if uploaded_file is not None:
#
#     # 将传入的文件转为Opencv格式
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     opencv_image = cv2.imdecode(file_bytes, 1)
#     # 展示图片
#     st.image(opencv_image, channels="BGR")
#
#     cv2.imwrite('test.png',opencv_image)
# 然后就可以用这个图片进行一些操作了



# 输入验证码地址
img_code_url=st.text_input("验证码地址")

# 将request 开启会话
session = requests.session()
if st.button("识别"):
    if "https://" in img_code_url  and img_code_url is not None:
    
        # 获取验证码图片地址
        png = session.get(url=img_code_url)  # 请求验证码

        ss = json.loads(ss)

        img_code_url1 = ss['data']["image"]

        try:
            # 截取uri的data:image/png;base64后端的uri
            img_code_url = img_code_url1.split(",")[1]
            # 这个就是解析
            ss = base64.b64decode(img_code_url)
            print(ss)
            
        except Exception as e:
            print(f"base64_to_img error:{e}")



        print(img_code_url)
       
        
        # 将验证码保存本地
        filename = "test.png"  # 定义一个图片地址
        file = open(filename, "wb")  # 以二进制打开一个文件
        file.write(png.content)  # 写入二进制文件
        file.close()  # 关闭文件


ocr = ddddocr.DdddOcr(show_ad=False) # 实例化

with open('test.png', 'rb') as f: # 打开图片

    img_bytes = f.read() # 读取图片
    res = ocr.classification(img_bytes) # 识别

    # 打印验证码
    print(res)
    st.text("验证码识别结果为："+res)
