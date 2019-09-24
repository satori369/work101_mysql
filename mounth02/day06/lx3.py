from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('127.0.0.1',8888))

while True:

    data,addr = s.recvfrom(1024)
    print(addr,data.decode())

    s.sendto(b'OK',addr)

s.close()