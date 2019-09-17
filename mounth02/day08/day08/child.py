from time import sleep
import os

def f1():
    for i in range(3):
        sleep(2)
        print("写代码")

def f2():
    for i in range(2):
        sleep(4)
        print("测代码")

pid = os.fork()
if pid == 0:  # 一级子进程
    p = os.fork()
    if p == 0:  # 二级子进程
        f1()
else:
    os.wait()
    f2()  # 父进程事件
