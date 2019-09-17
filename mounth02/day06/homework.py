from socket import *
# 创建udp套接字

sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
sockfd.bind(('127.0.0.1',8888))

# 循环收发消息
data,addr = sockfd.recvfrom(1024)
print(addr,data)

