"""
获取进程PID
"""

import os

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('Child PID:',os.getppid())
else:
    print('Parent PID',pid)
    os._exit()

