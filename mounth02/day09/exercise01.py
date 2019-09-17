import time
from multiprocessing import *

def timeit(zj):
    def sj(*args,**kwargs):
        t1=time.time()
        res = zj(*args,**kwargs)
        t2 = time.time()
        print('%s函数执行时长:%.6f'%(zhishu.__name__,t2-t1))
        return res
    return sj


def zhishu(n):
    # if n <= 1:
    #     return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# print(zhishu(10))
#
# @timeit
# def zj(n):
#     num=0
#     for i in range(2,n):
#         if zhishu(i):
#             num+=i
#     return num
#
# # print(zj(100000))

class Prime(Process):
    def __init__(self,prime,begin,end):
        super().__init__()
        self.prime = prime # 装质数的列表
        self.begin = begin # 开始位置
        self.end = end #结束位置

    def run(self):
        for i in range(self.begin,self.end):
            if zhishu(i):
                self.prime.append(i)
        sum(self.prime)

@timeit
def use_4_process():
    prime = []
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(prime,i,i+25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

@timeit
def use_10_process():
    prime = []
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

use_10_process()