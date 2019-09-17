'''
http请求响应演示
'''

from socket import *


#tcp服务端


def add(c):
    data = c.recv(4096).decode()
    # print('查看data',data,'结束')
    info = data.split('\n')[0].split(' ')[1]

    if info == '/':
        with open('index.html') as f:
            re = """HTTP/1.1 200 OK
                         Content-Type: text/html

                         """ + f.read()
    else:
        re = """HTTP/1.1 404 Not Found
                     Content-Type: text/html

                     <h1><u>Sorry</u></h1>
                     """
    c.send(re.encode())

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('176.215.133.193', 8000))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print('connect from',addr)
        add(c)

main()