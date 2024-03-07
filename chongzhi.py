import pymysql
from tkinter import *           # 导入 Tkinter 库

import tkinter as tk

root = tk.Tk()
root.geometry('600x200')

root.title('充值金额积分小工具')

def yue():
    # 创建数据库连接
    yue_conn = pymysql.connect(
        host='10.0.1.101',  # 连接主机, 默认127.0.0.1
        user='root',  # 用户名
        passwd='root',  # 密码
        port=3306,  # 端口，默认为3306
        db='aq_coupon',  # 数据库名称
        charset='utf8'  # 字符编码
    )
    # 生成游标对象 cursor
    cursor = yue_conn.cursor()
    userid=''

    sql="update t_user set recommend_amount=450 where user_id = '%d'"%(134376)

    try:
        cursor.execute(sql)
        yue_conn.commit()
    except:
        print("expection!")
        yue_conn.rollback()

    # 查看更新后的结果
    sql = "SELECT recommend_amount FROM t_user where user_id =134376"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

def jifen():
    # 创建数据库连接
    jifen_conn = pymysql.connect(
        host='10.0.1.101',  # 连接主机, 默认127.0.0.1
        user='root',  # 用户名
        passwd='root',  # 密码
        port=3306,  # 端口，默认为3306
        db='aq_jifen',  # 数据库名称
        charset='utf8'  # 字符编码
    )
    # 生成游标对象 cursor
    cursor = jifen_conn.cursor()
    userid = ''

    sql = "update user_jifen set  jifen_balance=132 where user_id='%d'" % (134376)

    try:
        cursor.execute(sql)
        jifen_conn.commit()
    except:
        print("expection!")
        jifen_conn.rollback()

    # 查看更新后的结果
    sql = "SELECT jifen_balance FROM user_jifen where user_id =134376"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)


lb = Label(root,text='用户id')
lb.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)


inp1 = Entry(root)
inp1.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)


# 金额
lb1 = Label(root,text='请输入充值金额')
lb1.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.1)
btn1 = Button(root, text='充值金额', command=yue)
btn1.place(relx=0.8, rely=0.2, relwidth=0.5, relheight=0.1)



# 积分
# btn2 = Button(root, text='充值分数', command=jifen)
# btn2.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.1)

lb.pack()
root.mainloop()








if __name__ == '__main__':
    aa=yue()
    bb=jifen()
