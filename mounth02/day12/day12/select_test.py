"""
select 演示
"""

from select import select
from socket import *

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

f = open('12.txt')

print(" 监控io ")
rs,ws,xs = select([s],[s],[s])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)
