"""
dict 服务端

* 处理业务逻辑
* 多进程并发模型
"""

from socket import *
from multiprocessing import Process
import sys,signal
from time import sleep

from mounth02.day17.dict_db import User

HOST = '127.0.0.1'
PORT = 8889
ADDR = (HOST,PORT)
db = User(database='dict')


# 注册逻辑
def do_register(connfd,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name,passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'Fail')

# 登录
def do_login(connfd,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name,passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'Fail')

# 查字典
def do_query(connfd,data):
    tmp = data.split(' ')
    name = tmp[1]
    word = tmp[2]
    mean = db.query(word)
    if not mean:
        connfd.send('没有找到该单词'.encode())
    else:
        db.insert_history(name, word)
        msg = "%s : %s"%(word,mean)
        connfd.send(msg.encode())

#历史记录
def do_history(connfd,data):
    name = data.split(' ')[1]
    r = db.history(name)
    print(r)
    for i in r:
        msg = '%s   %-16s   %s'%i
        connfd.send(msg.encode())
        sleep(0.1)
    connfd.send(b'##')

def request(connfd):
    db.create_cursor() # 每个子进程有自己的游标
    while True:
        data = connfd.recv(1024).decode()
        if not data or data[0] =='E':
            sys.exit() #退出对应子进程
        if data[0] == 'R':
            do_register(connfd,data)
        elif data[0] =='L':
            do_login(connfd,data)
        elif data[0] =='Q':
            do_query(connfd,data)
        elif data[0] == 'H':
            do_history(connfd,data)

def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    #处理僵尸
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen the port 8888...")
    while True:
        # 循环等待客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建线程
        p = Process(target=request,args=(c,))
        p.daemon = True
        p.start()

if __name__ == '__main__':
   main()
