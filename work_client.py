from socket import *

s = socket()

addr = ('127.0.0.1',8888)
s.connect(addr)

def select():
    i = input('1.bus1,2.bus2')
    n = input('输入姓名')
    i = 's ' + i + ' ' + n
    return i
def insert():
    i = input('1.bus1,2.bus2')
    if i == '1':
        n1 = input('输入车型')
        n2 = input('输入批次编号')
        n3 = input('输入VIN(int)')
        n4 = input('输入发动机型号(int)')
        n5 = input('输入验收日期(xxxx-xx-xx)')
        n6 = input('输入发运日期(xxxx-xx-xx)')
        n7 = input('输入单号(int)')
        n8 = input('输入接收单位')
        n9 = input('输入单位地址')
        n10 = input('输入姓名')
        n11 = input('输入电话(11位数字)')
        i = 'i ' + i + ' ' + n1 + ' ' + n2 + ' ' + n3 + ' ' + n4 + ' ' + n5 + ' ' + n6 + ' ' + n7 + ' ' + n8 + ' ' + n9 + ' ' + n10 + ' ' + n11
    # elif i=='2':
    #     n = input('输入姓名')
    return i

def update():
    i = input('1.bus1,2.bus2')
    n3 = input('修改谁的数据')
    n1 = input('输入要修改的字段')
    n2 = input('要改的值')
    i = 'u ' + i + ' ' + n1 + ' ' + n2 + ' ' + n3
    return i

def delete():
    i = input('1.bus1,2.bus2')
    n1 = input('删除谁的数据')
    i = 'd ' + i + ' ' + n1
    return i

def main():
    while True:
        i = input('1查询,2插入,3修改,4删除')
        if not i:
            break
        elif i=='1':
            i = select()
        elif i=='2':
            i = insert()
        elif i=='3':
            i = update()
        elif i == '4':
            i = delete()

        s.send(i.encode())
        data = s.recv(1024).decode()
        print(data)


if __name__ == '__main__':
    main()
