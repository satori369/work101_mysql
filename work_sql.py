"""
数据库处理操作
"""

import pymysql

class User:
    def __init__(self,host='localhost',port = 3306,user = 'root',passwd = '781124',database = None,charset = 'utf8'):
        self.host = host
        self.port = port
        self.passwd = passwd
        self.user = user
        self.charset = charset
        self.database = database
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,port=self.port,user=self.user, password=self.passwd,database=self.database,charset = self.charset)

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()  # 游标

    #查单词
    def select(self,table,name):
        sql = "select * from %s where name='%s';"%(table,name)
        self.cur.execute(sql)
        r = self.cur.fetchall()
        if r:
            return r

    def insert(self,table,word):
        table=(table,)
        word=table+word
        sql = "insert into %s (chexing,picibianhao,VIN,fadongji,yanshoudate,fayundate,danhao,jsdanwei," \
              "danweidizhi," \
              "name," \
                   "tel)values ('%s','%s',%s,%s,'%s','%s',%s,'%s','%s','%s',%s);"%word
        self.cur.execute(sql)
        self.db.commit()

    def update(self,table,word):
        table = (table,)
        word = table + word
        print(word)
        sql = "update %s set %s=%s where name='%s';" % word
        self.cur.execute(sql)
        self.db.commit()

    def delete(self,table,word):
        table = (table,)
        word = table + word
        print(word)
        sql = "delete from %s where name='%s';"%word
        self.cur.execute(sql)
        self.db.commit()

if __name__ == '__main__':
    db = User(database='bus')
    db.create_cursor()

    c = ('danhao', '456', 'name', '王五')
    db.update('bus1',c)

    # table='bus1'
    # word = ('12','12','35','645','1885-5-1','1448-10-5','123','12','12','ff','14505050404')
    # # sqlt = "insert into %s" % table
    # # sql = sqlt + "(chexing,picibianhao,VIN,fadongji,yanshoudate,fayundate,danhao,jsdanwei,danweidizhi,name,tel)values ('%s','%s',%s,%s,'%s','%s',%s,'%s','%s','%s',%s);" % word
    # db.insert(table,word)


