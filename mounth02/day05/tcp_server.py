"""
tcp_server.py   tcp套接字服务端流程
重点代码

注意: 功能性代码,注重流程和函数使用
"""

import socket

#创建流式套接字对象
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('176.215.133.193',8888))

#设置监听
sockfd.listen(5)

while True:
#等待处理客户端连接请求
    print('waiting for connect...')
    try:
        connfd,addr = sockfd.accept()
        print('Connect from',addr)
    except KeyboardInterrupt:
        print('Sever exit')
        break
    except Exception as e:
        print(e)
        continue

    #消息收发
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive:",data.decode())
        n = connfd.send('收到'.encode())
        print('Send %d bytes' %n)
    #关闭套接字
    # jx=input('按任意键继续\n退出连接按2')
    # if jx=='2':
    #     break
    connfd.close()

sockfd.close()
