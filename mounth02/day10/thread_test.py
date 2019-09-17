"""
测试用例
"""
from threading import Lock,Thread
from multiprocessing import Process
import time

# 计算
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# io
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1700000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()

######单进程CPU操作
# t1 = time.time()
# for i in range(10):
#
#     count(1,1)
#
# t2 = time.time()-t1
# print(t2)

######单进程IO操作
# 8.452343225479126
# t1 = time.time()
# for i in range(10):
#
#     io()
# t2 = time.time()-t1
# print(t2)
# 4.505939722061157


######多线程CPU操作
# t1 = time.time()
# jobs = []
# for i in range(10):
#     t = Thread(target=count,args= (1,1))
#     jobs.append(t)
#     t.start()
#
# for i in jobs:
#     i.join()
#
# print(time.time()-t1)
# 13.596534967422485


######多线程IO操作
# t1 = time.time()
# jobs = []
# for i in range(10):
#     t = Thread(target=io)
#     jobs.append(t)
#     t.start()
#
# for i in jobs:
#     i.join()
#
# print(time.time()-t1)

######多进程CPU操作
# 52.55716586112976
# t1 = time.time()
# jobs = []
# for i in range(10):
#     t = Process(target=io)
#     jobs.append(t)
#     t.start()
#
# for i in jobs:
#     i.join()
#
# print(time.time()-t1)
# 2.167501211166382

######多进程IO操作
# t1 = time.time()
# jobs = []
# for i in range(10):
#     t = Process(target=count,args=(1,1))
#     jobs.append(t)
#     t.start()
#
# for i in jobs:
#     i.join()
#
# print(time.time()-t1)
# 3.9997899532318115
