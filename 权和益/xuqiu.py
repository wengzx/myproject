import  requests
import streamlit as st

# 所有需求


class xuqiu():


    # 需求地址列表
    xuqiulist={
        "数据大屏":"https://odrylr.axshare.com/?id=zmyo43&p=%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%90%8E%E5%8F%B0",
        "畅游需求":"https://z5m64t.axshare.com/?id=7ntcx7&p=h5%E7%99%BB%E5%BD%95%E9%A1%B5%E9%9D%A2&g=1"

    }


    def xuqiu(self):
        pp=[]
        for key in self.xuqiulist:
            datas=key+ ":"+self.xuqiulist[key]
            pp.append(datas)

            print(key, ":", self.xuqiulist[key])
        return pp


if st.button("点击查看需求地址"):
    aa=xuqiu()
    bb=aa.xuqiu()
    for p  in bb:
        st.write(p)
