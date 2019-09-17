"""
multiprocessing 模块创建进程
1. 编写进程执行函数
2. 创建进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
from time import sleep

#进程函数
def fun():
    print('开始一个进程')
    sleep(3)
    print('进程结束')

#创建进程对象
p = mp.Process(target = fun)
p.start()# 启动进程
sleep(2)
print('父进程')
p.join()# 回收进程

'''
p = os.fork()
if pid == 0:
    fun()
else:
    os.wait()
'''