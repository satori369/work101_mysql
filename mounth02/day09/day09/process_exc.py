"""
求100000以内所有质数之和
 请分别用单进程，4进程，10进程完成
记录每种情况的执行时间 通过装饰器记录时间

"""
from multiprocessing import Process
from timeit import timeit

# 判断一个数是否是质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n)):
        if n % i == 0:
            return False
    return True

# 单进程 no_multi_process函数执行时长:26.169546
# @timeit
# def no_multi_process():
#     prime = []
#     for i in range(1,100001):
#         if isPrime(i):
#             prime.append(i)
#     print(sum(prime))
#
# no_multi_process()

# 自定义进程类
class Prime(Process):
    def __init__(self,prime,begin,end):
        super().__init__()
        self.prime = prime  # 装质数的列表
        self.begin = begin  # 开始位置
        self.end = end  # 结束位置

    def run(self):
        for i in range(self.begin,self.end):
            if isPrime(i):
                self.prime.append(i)
        sum(self.prime)


#4个进程 use_4_process函数执行时长:15.554102
# @timeit
# def use_4_process():
#     prime = []
#     jobs = []
#     for i in range(1,100001,25000):
#         p = Prime(prime,i,i+25000)
#         jobs.append(p)
#         p.start()
#     [i.join() for i in jobs] # 回收进程
#
# use_4_process()


# 10 进程 use_10_process函数执行时长:13.969181
@timeit
def use_10_process():
    prime = []
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs] # 回收进程

use_10_process()


