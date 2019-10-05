'''
创建库和表
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

# 创建库(指定字符集)
# create database 库名 [character set utf8];
# create database 库名 charset=utf8;

# 创建表(指定字符集)
# create table 表名(
# 字段名 数据类型,
# ...);

# 如果你想设置数字为无符号则加上 unsigned
# 如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL。
# DEFAULT 表示设置一个字段的默认值
# AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
# PRIMARY KEY关键字用于定义列为主键。主键的值不能重复。

# 创建库
sql = "create database work101_bus charset=utf8;"

# 创建表
# sql = "create table bus2 (序号 int auto_increment primary key, 维修时间 date,装备所在单位 varchar(64),维修地址 varchar(64),故障现象 varchar(64),故障原因 varchar(128),故障排除方式 varchar(32),设备使用情况 varchar(32),装备使用频率 varchar(32),是否经历过大型演习 varchar(32));"
cur.execute(sql)  # 执行语句

# 提交到数据库
db.commit()

# 关闭游标
cur.close()

# 关闭数据库
db.close()
