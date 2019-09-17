import signal
from time import sleep
import os

#信号处理僵尸
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print('Create process failed')
elif pid == 0:
    # sleep(3)
    print('The new process')
else:
    # sleep(4)
    print('The old process')
    while True:
        pass

