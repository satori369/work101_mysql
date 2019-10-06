## 1. windows环境

**cmd命令**

>dir查看目录

>set PATH=%PATH%;D:\Python   设置系统变量python

>set PATH=%PATH%;D:\Python\Scripts  设置系统变量pip

---

## 2. mysql

   * 数据库操作
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

##tcp/udp
- socket      套接字
  - **AF_INET,SOCK_STREAM**
  - **AF_INET,SOCK_DGRAM**
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
