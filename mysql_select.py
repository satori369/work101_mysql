'''
查
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

# 获取数据
sql="select * from bus2;"
cur.execute(sql)

# 可以直接遍历游标
for i in cur:
    print(i)

# 获取所有查询结果
# all_row = cur.fetchall()
# print(all_row)

# 获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)

# 获取一个查询结果
# one_row = cur.fetchone()
# print(one_row)
#
cur.close()
db.close()