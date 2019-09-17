from socket import *
import struct

def dabao(id,name,age,score):
    st = struct.Struct('i16sif')
    xx = st.pack(id,name.encode(),age,score)
    return xx
#
# In [4]: data
# Out[4]: b'\x01\x00\x00\x00Abby\x9a\x99\xd9?'
#
# In [5]: st.unpack(data)
# Out[5]: (1, b'Abby', 1.7000000476837158)
#
# In [6]:

ADDR = ('176.215.133.193',8888)

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    id = int(input('学号:'))
    name = input('姓名:')
    age = int(input('年龄:'))
    score = float(input('分数:'))
    if not (id and name and age and score):
        break
    sockfd.sendto(dabao(id,name,age,score),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print('From server:',msg.decode())

sockfd.close()
