"""
epoll_server.py
"""

from socket import *
from select import *

# 创建套接字作为关注IO
s = socket()
s.setsockopt(1,2,1)
s.bind(('127.0.0.1',8888))
s.listen(3)

# 创建poll对象
ep = epoll()

# 建立查找字典,通过IO对象的fileno找到对象
# 字典内容与关注IO保持一致{fileno:io_obj}
fdmap = {s.fileno():s}

# 关注s
ep.register(s,EPOLLIN|EPOLLERR)

# 循环监控IO的发生
while True:
    events = ep.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from',addr)
            # 添加新的关注对象,同时维护字典
            ep.register(c,EPOLLIN|EPOLLET)# ET边缘触发
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            # p.register(fd,EPOLLOUT)
            fdmap[fd].send(b'OK')
        # elif event & EPOLLOUT:
        #     p.register(fd, EPOLLIN)