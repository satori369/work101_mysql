from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.connect(('127.0.0.1',8888))


while True:
    data = input('>>')
    if not data:
        break
    s.send(data.encode())
    c = s.recv(1024).decode()
    print(c)

s.close()