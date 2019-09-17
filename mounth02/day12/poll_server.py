"""
poll_server.py  方法实现IO多路复用
重点代码

【1】创建套接字
【2】将套接字register
【3】创建查找字典,并维护
【4】循环监控IO发生
【5】处理发生的IO
"""

from socket import *
from select import *

# 创建套接字作为关注IO
s = socket()
s.setsockopt(1,2,1)
s.bind(('127.0.0.1',8889))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典,通过IO对象的fileno找到对象
# 字典内容与关注IO保持一致{fileno:io_obj}
fdmap = {s.fileno():s}

# 关注s
p.register(s,POLLIN|POLLERR)

# 循环监控IO的发生
while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from',addr)
            # 添加新的关注对象,同时维护字典
            p.register(c,POLLIN)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            p.register(fd,POLLOUT)
            # fdmap[fd].send(b'OK')
        elif event & POLLOUT:
            p.register(fd, POLLIN)