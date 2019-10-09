from socket import *
from multiprocessing import Process
from mysql.work101_mysql.work_sql import User
import sys

db = User(database='bus')

def chaxun(c, data):
    ds=data.split(' ')
    if ds[1]=='1':
        dse = db.select('bus1',ds[2])
        if dse:
            msg='id:%s\n车型:%s\n批次编号:%s\nVIN:%s\n发动机型号:%s\n验收时间:%s\n发运时间:%s\n单号:%s\n接收单位:%s\n接收地址:%s\n姓名:%s\n电话:%s'%dse[0]
            c.send(msg.encode())
        else:
            c.send('没有这个名字'.encode())

    if ds[1]=='2':
        dse = db.select('bus2', ds[2])
        if dse:
            msg = '序号:%s\n维修时间:%s\n装备所在党委:%s\n维修地址:%s\n故障现象:%s\n故障原因:%s\n故障排除方式:%s\n设备使用情况:%s\n装备使用频率:%s\n是否经历过大型演习:%s\n姓名:%s'% dse[0]
            c.send(msg.encode())
        else:
            c.send('没有这个名字'.encode())

def tianjia(c, data):
    print(data)
    ds = data.split(' ')
    word = (ds[2],ds[3],ds[4],ds[5],ds[6],ds[7],ds[8],ds[9],ds[10],ds[11],ds[12])
    print(word)
    if ds[1] == '1':
        db.insert('bus1', word)
        c.send(b'OK')

def shoufa(c):
    db.create_cursor()
    while True:
        data = c.recv(1024).decode()
        if not data:
            sys.exit()
        if data[0] == 's':
            chaxun(c, data)
        elif data[0] == 'i':
            tianjia(c, data)
        # elif data[0] == 'Q':
        #     do_query(connfd, data)
        # elif data[0] == 'H':
        #     do_history(connfd, data)

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('127.0.0.1',8888))
    s.listen(5)

    while True:
        print('等待连接')
        try:
            c, addr = s.accept()
        except KeyboardInterrupt:
            print('服务器断开')
            break
        except Exception:
            continue

        p = Process(target=shoufa, args=(c,))
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()
