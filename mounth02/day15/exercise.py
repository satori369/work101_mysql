import pymysql


db = pymysql.connect(user = 'root',
                     passwd = '123456',
                     database = 'dict',
                     charset = 'utf8')
cur = db.cursor()

sql = "insert into words (word,mean) values (%s,%s)"

f = open('dict.txt','r')
for i in f:
    fr = i.split(' ',1)
    word = fr[0]
    mean = fr[1].strip()
    cur.execute(sql,[word,mean])

try:
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()