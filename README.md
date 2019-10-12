## 1. 操作环境

**cmd命令**

>dir查看目录

>set PATH=%PATH%;D:\Python   设置系统变量python

>set PATH=%PATH%;D:\Python\Scripts  设置系统变量pip
> pip install pymysql

**liunx命令**

```liunx
系统命令         安装
sudo apt-get install unrar;sudo apt-get install unrar 下载压缩包
unrar x 文件名(rar) 解压

自家执行
pip3 install celery
pip3 freeze|grep 'Django'
版本不是1.11.8, 执行
pip3 uninstall Django
pip3 install Django==1.11.8


sudo su 切换超级权限
cd /var/lib/mysql-files/  mysql安全文件目录
ll(ls -l) 查看目录下文件的详细信息
chmod 666 scoreTable.csv 打开读写权限


```
rm -fr *  ???????????????????????????

---

## 2. mysql


```mysql
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
    
    select * from mysql.user\G; 看用户
```
    
   * 数据库操作
     - Navicat premium 数据库界面工具
     - source ./bus.sql;导入路径里的表
     - show databases;
     - create database  [db_name];
     - select database();
     - use [db]
     - show create database [db];
     - drop database [db];
   * 数据表
    - show--- tables;
    - create--- table--- [tb_name]--- (column1 type,...);
   * 字段约束
	   - primary key
	   -  auto_increment
	   -  not null
	   -  default [val]
	   -  unsigned
   - 数据类型
       - 数字 （整数，小数，布尔）
       - 字符串 （char varchar blob text enum set）
       - 时间日期
    - desc [tb]
    -  show create table [tb]
    - drop table [tb]
* 增删改查
   - insert into [tb] [col,col...] values (val1,val2),();
   - delete from [tb] where...;
   - update [tb] set ... where ...;
   - select [col...] from  [tb] where ...;
   - where 子句 ： 算数  逻辑  比较  位运算
* 表结构修改
     - 语法 ：alter table 表名 执行动作;
     - 添加字段(add)
       - alter table 表名 add 字段名 数据类型;
       - alter table 表名 add 字段名 数据类型 first;
       - alter table 表名 add 字段名 数据类型 after 字段名;
     - 删除字段(drop)
        - alter table 表名 drop 字段名;
     - 修改数据类型(modify)
        - alter table 表名 modify 字段名 新数据类型;
     - 修改字段名(change)
        - alter table 表名 change 旧字段名 新字段名 新数据类型;
     - 表重命名(rename)
        - alter table 表名 rename 新表名;

---

## 3. tcp/udp
- socket      套接字
  - **AF_INET,SOCK_STREAM**TCP
  - **AF_INET,SOCK_DGRAM**UDP
- HOST        主人
- PORT        端口
- ADDR        地址
- setsockopt  设置超时  
  **- SOL_SOCKET,SO_REUSEADDR**
- 设置监听列表(tcp)
	- bind        绑定
	- listen      接听
	- accept      接受  connect  连接
	- except      除...之外
- recv        收到   recvfrom
- send        发送   sendto
- close       关闭
- 250919354郭
- 牛客网