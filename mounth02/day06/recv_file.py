'''
接受文件
'''

from socket import *

s = socket()

s.bind(('127.0.0.1',8888))
s.listen(3)
