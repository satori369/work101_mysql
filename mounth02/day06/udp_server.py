'''
udp_server.py  udp套接字服务端流程
重点代码
'''

from socket import *
import struct

st = struct.Struct('i16sif')


# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

##############端口立即重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 绑定地址
server_addr = ('176.215.133.193',8888)
sockfd.bind(server_addr)

f = open('student.txt','a')

# 循环收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    data = st.unpack(data)
    # def caibao():
    #     list=[]
    #     for item in st.unpack(data):
    #         if type(item) == bytes:
    #             item = item.decode()
    #         list.append(item)
    #     return list

    # print('Msg from %s:%s'% (addr,caibao()))
    info = "%d  %-10s  %d  %.1f\n" % data
    f.write(info)
    f.flush()
    sockfd.sendto(b'Thanks',addr)


# 关闭套接字
f.close()
sockfd.close()
