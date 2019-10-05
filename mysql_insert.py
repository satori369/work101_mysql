'''
增
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

'''
bus1
'''
# 插入全部数据
# sql = "insert into bus1 values (2,'J1','Q2017-01#','456',4567,'2009-10-2','2009-11-2',45678,'123部队','湖北省荆州市','李四',17307160552);"

# 插入所选字段数据
# sql = "insert into bus1 (chexing,picibianhao,yanshoudate,fayundate,jsdanwei,danweidizhi,name)values ('J3','D2017-01#','2012-10-2','2012-11-2','110部队','台湾省广岛市','陈七');"
# cur.execute(sql)  # 执行语句

'''
bus2
'''
sql = "insert into bus2 (维修时间,装备所在单位,维修地址,故障现象) values ('2019-7-5','456部队','四川省成都市','无法着车');"
cur.execute(sql)
# 提交到数据库
db.commit()

# 关闭游标
cur.close()

# 关闭数据库
db.close()
