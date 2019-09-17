'''
udp_client.py  udp客户端
重点代码
'''

from socket import *

# 服务器地址
ADDR = ('176.215.133.14',6666)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发消息
while True:
    data = input('msg>>')
    if not data: # 退出
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print('From server:',msg.decode())

sockfd.close()