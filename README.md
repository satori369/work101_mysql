#aid1907
~~~~
mounth02

###process_server.py 多进程并发模型day11

from socket import *

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen the port 8888...")
while True:
    # 循环等待客户端连接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt as e:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建进程
    p = Process(target=handle,args=(c,))
    p.daemon = True
    p.start()
    
# 客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()