'''
gevent server 基于协程的tcp并发
'''
import gevent
from gevent import monkey
monkey.patch_all() # 执行脚本修改socket阻塞行为
from socket import *


def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            return
        print(data)
        c.send(b'OK')

# 创建套接字
s = socket()
s.setsockopt(1,2,1)
s.bind(('127.0.0.1',8889))
s.listen(5)

# 循环接收来自客户端请求
while True:
    c,addr = s.accept()
    print('Connect from',addr)
    gevent.spawn(handle,c) # 协程方案