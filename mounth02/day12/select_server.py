"""
select tcp 服务
重点代码

【1】 将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表,确定就绪IO事件
【4】处理发生的IO事件
"""

from socket import *
from select import select

# 创建监听套接字作为关注IO
s = socket()
s.setsockopt(1,2,1)
s.bind(('127.0.0.1',8889))
s.listen(3)

# 设置关注列表
rlist = [s] # 等待客户端连接
wlist = []
xlist = []

# 监控IO发生
while True:
    rs,ws,xs, = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print('Connect from',addr)
            rlist.append(c)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r) # 取消关注
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        wlist.remove(w)