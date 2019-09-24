from socket import *

s = socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

ADDR = ('127.0.0.1',8888)
s.bind(ADDR)

s.listen(5)

while True:
    print('等待链接')
    try:
        c,addr = s.accept()
        print('连接上',addr)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        continue

    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()

s.close()