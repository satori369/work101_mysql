"""
read_db.py
pymysql 读操作演示  (select)
"""
import pymysql
# 链接数据库
db = pymysql.connect(user = 'root',passwd = '123456',database = 'stu',charset = 'utf8')

# 获取游标
cur = db.cursor()

# 获取数据
sql = 'select name,hobby from interest where hobby = "draw";'

cur.execute(sql)

# 可以直接遍历游标
# for i in cur:
#     print(i)

# 查询所有结果
# all_row = cur.fetchall()
# print(all_row)

# 获取多个查询结果
# many_row = cur.fetchmany(1)
# print(many_row)

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)




# 关闭游标
cur.close()

# 关闭数据库
db.close()