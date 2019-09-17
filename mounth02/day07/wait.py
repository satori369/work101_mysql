'''
wait.py  处理僵尸进程的方法
'''

import os

pid = os.fork()

if pid<0:
    print('Error')
elif pid == 0:
    print('Child process:',os.getpid())
    os._exit(1)
else:
    pis,status = os.wait() #阻塞等待回收子进程
    print('pid:',pid)
    print('status:',status)
    while True:#让父进程不退出
        pass