'''
改
'''
import pymysql

db = pymysql.connect(host='localhost',
                     port = 3306,
                     user='root',
                     password = '781124',
                     database = 'work101_bus',
                     charset='utf8')

# 获取游标 (操作数据库,执行sql语句,得到执行结果)
cur = db.cursor()

# update 表名 set 字段1=值1,字段2=值2,... where 条件;
for i in range(6,7):
    u = i-1
    sql = "update bus1 set id=%d where id=%d;" % (u, i)
    cur.execute(sql)  # 执行语句

    # 提交到数据库
    db.commit()

# 关闭游标
cur.close()

# 关闭数据库
db.close()
