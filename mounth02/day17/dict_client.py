"""
dict 客户端
"""

from socket import *
import sys
import getpass


#服务器地址
ADDR = ('127.0.0.1',8889)
s = socket()
s.connect(ADDR)
# 注册
def do_register():
    while True:
        name = input('User:')
        pwd = getpass.getpass()
        pwd1 = getpass.getpass('Again:')
        if pwd != pwd1:
            print('两次密码不一致!')
            continue
        if (' ' in name) or (' ' in pwd):
            print('用户名或密码不能含有空格')
            continue

        msg = 'R %s %s'%(name,pwd)
        s.send(msg.encode()) # 发送请求
        data = s.recv(128).decode() # 反馈
        if data == 'OK':
            print('注册成功')
            main2(name)
        else:
            print('注册失败')
        return

# 登录
def do_login():
        name = input('User:')
        pwd = getpass.getpass()

        msg = 'L %s %s' % (name, pwd)
        s.send(msg.encode())  # 发送请求
        data = s.recv(128).decode()  # 反馈
        if data == 'OK':
            print('登录成功')
            main2(name)
        else:
            print('用户名或密码错误')


# 查字典
def do_query(name):
    while True:
        word = input('输入要查询的单词:')
        if word == '##':
            break
        msg = 'Q %s %s' % (name,word)
        s.send(msg.encode())  # 发送请求
        data = s.recv(2048).decode()  # 反馈
        print(data)


#历史记录
def do_history(name):
    msg = 'H ' + name
    s.send(msg.encode())
    while True:
        data = s.recv(1024).decode()
        if data == '##':
            break
        print(data)

#搭建网络
def main():

    while True:
        print('\n=========command========')
        print('*****    1.注册     *****')
        print('*****    2.登录     *****')
        print('*****    3.退出     *****')
        print('========================')
        cmd = input('选项(1,2,3):')
        s.send(cmd.encode())
        if cmd == '1':
            do_register()
        elif cmd =='2':
            do_login()
        elif cmd =='3':
            s.send(b'E')
            sys.exit('谢谢使用')
        else:
            print('请输入正确命令')

def main2(name):
    while True:
        print('\n=========command========')
        print('*****    1.查单词    *****')
        print('*****    2.历史记录  *****')
        print('*****    3.注销      *****')
        print('========================')
        cmd = input('选项(1,2,3):')
        s.send(cmd.encode())
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_history(name)
        elif cmd == '3':
            return # 二级界面结束
        else:
            print('请输入正确命令')

if __name__ == '__main__':
    main()