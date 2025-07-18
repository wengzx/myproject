import pymysql


db=pymysql.connect(host="10.0.1.101",user="root",password="root",database="aq_jifen")

cursor=db.cursor()

sql="select * from user_jifen where user_id = 134266"

cursor.execute(sql)
0000
aa=cursor.fetchone()

op=list(aa)
print(op)
if sql:
    print(aa[1])

db.commit()

cursor.close()
db.close()


