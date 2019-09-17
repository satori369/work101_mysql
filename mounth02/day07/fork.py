'''
fork.py  fork进程演示1
'''
from time import sleep
import os

pid = os.fork()
if pid < 0:
    print('Create process failed')
elif pid == 0:
    # sleep(3)
    print('The new process')
else:
    # sleep(4)
    print('The old process')

print(pid)