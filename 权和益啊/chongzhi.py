import pymysql
import streamlit as st


class update_jifen_yue():


    def yue(self,userid,yuer):
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
        userid=int(userid)


        sql="update t_user set recommend_amount='%s' where user_id = '%d'"%(yuer,userid)
        print(sql)

        try:
            cursor.execute(sql)
            yue_conn.commit()
        except:
            print("expection!")
            yue_conn.rollback()

        # 查看更新后的结果
        sql2 = "SELECT recommend_amount FROM t_user where user_id ='%s'"%(userid)
        print(sql2)
        cursor.execute(sql2)
        data = cursor.fetchall()
        print(data)

    def jifen(self,userid,jifen):
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
        userid = int(userid)

        # 查询语句
        select_sql = "SELECT jifen_balance FROM user_jifen where user_id ='%s'" % (userid)

        # 插入语句
        insert_sql = "INSERT INTO user_jifen(user_id) VALUES ('%s')" % (userid)

        # 更新语句
        update_sql = "update user_jifen set  jifen_balance='%s' where user_id='%d'" % (jifen, userid)

        print(select_sql)
        cursor.execute(select_sql)
        data = cursor.fetchall()
        if len(data) == 0:

            # 查询没有先插一条数据
            print("没数据,开始插入数据")


            print(insert_sql)
            cursor.execute(insert_sql)
            jifen_conn.commit()
            print("插入数据成功")


            # 然后再更新
            # update_sql = "update user_jifen set  jifen_balance='%s' where user_id='%d'" %(jifen,userid)
            # print(update_sql)
        else:
            try:
                # 执行更新用户积分
                cursor.execute(update_sql)
                jifen_conn.commit()
            except:
                # 异常处理
                print("expection!")
                jifen_conn.rollback()

        # 查询用户积分
        cursor.execute(select_sql)
        select_data = cursor.fetchall()
        print(select_data)


    #门店余额更新
    def vip(self,userid,suid,shop_amount):
        # 创建数据库连接
        vip_conn = pymysql.connect(
            host='10.0.1.101',  # 连接主机, 默认127.0.0.1
            user='root',  # 用户名
            passwd='root',  # 密码
            port=3306,  # 端口，默认为3306
            db='aq_coupon',  # 数据库名称
            charset='utf8'  # 字符编码
        )
        # 生成游标对象 cursor
        cursor = vip_conn.cursor()
        userid = int(userid)

        # 查询语句
        select_sql = "select shop_amount from aq_coupon.t_user_shop_vip where  user_id ='%s'" % (userid)

        # 插入语句
        insert_sql = "INSERT INTO user_jifen(user_id,suid) VALUES ('{0}','{1}')".format(userid, shop_amount)

        # 更新语句
        update_sql = "UPDATE t_user_shop_vip SET total_amount =%s, shop_amount =%s where user_id=%s and suid=%s"%(shop_amount,shop_amount, userid,suid)

        print(select_sql)
        cursor.execute(select_sql)
        data = cursor.fetchall()
        if len(data) == 0:
            # 查询没有先插一条数据
            print("没数据,开始插入数据")

            print(insert_sql)
            cursor.execute(insert_sql)
            vip_conn.commit()
            print("插入数据成功")


        else:
            try:
                # 执行更新用户积分
                cursor.execute(update_sql)
                vip_conn.commit()
            except:
                # 异常处理
                print("expection!")
                vip_conn.rollback()

        # 查询用户积分
        cursor.execute(select_sql)
        select_data = cursor.fetchall()
        print(select_data)

userid=st.text_input("请输入用户id")
jifen=st.text_input("请输入更新积分")
yuer=st.text_input("请输入更新余额")
suid=st.text_input("请输入门店")
shop_amount=st.text_input("请输入门店余额")



if st.button("更新余额和积分"):
    aa=update_jifen_yue()
    # aa.yue(userid,yuer)
    # aa.jifen(userid,jifen)
    aa.vip(userid,suid,shop_amount)








