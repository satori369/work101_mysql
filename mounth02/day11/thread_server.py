"""
thread_verver.py  基于fork多进程并发
重点代码

1. 创建监听套接字
2. 循环等待客户端连接
3. 客户端连接创建新的线程为客户端服务
4. 主线程继续等待其他客户端连接
5. 客户端退出,对应的分支线程退出
"""
from socket import *
from threading import Thread
import sys

#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

while True:
    # 循环等待客户端连接
    try:
        c,addr = s.accept()
        print('Connect from',addr)
    except KeyboardInterrupt as e:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建线程
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True) #设置当主线程退出时分支线程随之退出
    t.start()
