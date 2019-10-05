'''
删
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

# delete from 表名 where 条件;
sql = "delete from bus1 where chexing='J4';"
cur.execute(sql)  # 执行语句

# 提交到数据库
db.commit()

# 关闭游标
cur.close()

# 关闭数据库
db.close()
