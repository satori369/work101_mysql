"""
write_db.py
pymysql 写操作演示 ()
"""
import pymysql

# 链接数据库
db = pymysql.connect(user = 'root',
                     passwd = '123456',
                     database = 'stu',
                     charset = 'utf8')

# 获取游标
cur = db.cursor()

# 执行sql语句
# name = input('name:')
# age = int(input('age:'))
# gender = input('gender:')
# score = float(input('score:'))

# sql = "insert into class1 (name,age,gender,score) values ('%s',%d,'%s',%f);"%(name,age,gender,score)
# cur.execute(sql)
#
#
# db.commit() #同步到数据库
try:
    # sql = "insert into class1 (name,age,gender,score) values (%s,%s,%s,%s)"
    #
    # cur.execute(sql,[name,age,gender,score])

    # 修改操作
    sql = 'update class1 set score = 82 where name = "Abby"'
    cur.execute(sql)

    sql = "delete from class1 where name = 'tom'"
    cur.execute(sql)

    db.commit()
except Exception as e:
    print(e)
    db.rollback()


cur.close()
db.close()