"""
进程对象属性
"""
from multiprocessing import Process
import time

def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

p = Process(target=tm,name = "Tedu")

p.daemon = True # 父进程退出子进程随之退出

p.start()
time.sleep(2)
print("Name:",p.name)
print("PID:",p.pid)  # 进程PID
print("is alive:",p.is_alive())
