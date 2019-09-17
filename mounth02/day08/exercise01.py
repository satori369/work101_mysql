from socket import *


server_addr = ('127.0.0.1',8887)
dict = {'管理员':server_addr}


def cjyhm(s,name,addr):
    while True:
        if name in dict:
            s.sendto('用户名重复'.encode(), addr)
        else:
            print("%s:创建了用户名:%s" % (addr, name))
            s.sendto('您已进入聊天室'.encode(), addr)
            msg = "\n欢迎 %s 加入群聊" % name
            for i in dict:
                s.sendto(msg.encode(), dict[i])
            dict[name] = addr
            break



# 退出聊天室
def tuichu(name,addr):
    while True:
        data,addr = sockfd.recvfrom(1024)
        if not data:
            del dict[name]
            for c in dict:
                sockfd.sendto('%s退出了聊天室'.encode() % name, dict[c])
                break

def fsxx(data,addr):
    pid = os.fork()
    while True:
        data,addr = sockfd.recvfrom(1024)
        if pid < 0:
            print('Error')
        elif pid == 0:
            for item in dict:
                sockfd.sendto('%s:%s'.encode() % (name, data), dict[item])
        else:
            print("Msg from %s: %s" % (addr, data.decode()))

def kzq(s):
    data, addr = s.recvfrom(1024)
    tmp = data.decode().split(' ',2)
    if tmp[0]=='c':
        cjyhm(s,tmp[1],addr)
    elif tmp[0]=='s':
        pass
    elif tmp[0]=='q':
        pass
def cj():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(server_addr)
    kzq(s)

if __name__ == '__main__':
    cj()