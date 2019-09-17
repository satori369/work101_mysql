"""
udp_client.py udp客户端
重点代码
"""

from socket import *
import os

# 服务器地址
ADDR = ("127.0.0.1",8887)


# 创建套接字

# # 循环收发消息
# while True:
#     # sockfd.sendto(b'jin ru',ADDR)
#     data = input(">>")
#     if not data: # 退出
#         break
#     sockfd.sendto(data.encode(),ADDR)
#     msg,addr = sockfd.recvfrom(1024)
#     print(msg.decode())
#
# sockfd.close()
def fasong():
    pass

def jieshou():
    pass

def main():
    sockfd = socket(AF_INET, SOCK_DGRAM)
    while True:
        data = input("创建用户名>>")
        data ='c '+data
        sockfd.sendto(data.encode(), ADDR)
        msg, addr = sockfd.recvfrom(128)
        if msg.decode()=='欢迎%s进入聊天室'%data:
            print('您已进入聊天室')
            break
        else:
            print(msg.decode())

    f= os.fork()
    if f<0:
        print('Error')
    elif f == 0:
        fasong()
    else:
        jieshou()


if __name__ == '__main__':
    main()