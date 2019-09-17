import pymysql

# 链接数据库
db = pymysql.connect(user = 'root',
                     passwd = '123456',
                     database = 'stu',
                     charset = 'utf8')

# 获取游标
cur = db.cursor()

# 执行sql语句
name = input('name:')
password = input('password:')

try:
    sql = "insert into user (name,password) values (%s,%s)"

    cur.execute(sql,[name,password])
    db.commit()
except Exception as e:
    print(e)
    print('用户名重复')
    db.rollback()

cur.close()
db.close()