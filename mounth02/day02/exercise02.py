#将一个队列中的数据进行反转
# 3 4 1 6 5 8
# 8 5 6 1 4 3
from mounth02.day02.lstack import LStack
from mounth02.day02.squeue import *

sq=SQueue()
ls=LStack()

for i in range(15):
    sq.enqueue(i)

while not sq.is_empty():
    ls.push(sq.dequeue())

while not ls.is_emtpy():
    sq.enqueue(ls.pop())

while not sq.is_empty():
    print(sq.dequeue())