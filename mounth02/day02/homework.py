"""
lqueue.py 链式队列
重点代码
D G E B H F C A
思路分析:
1. 基于链表构建队列模型
2. 链表的头作为队头,尾作为队尾
3. 定义两个标记标记队头和队尾
4. 头和尾代表同一个无用节点时队列为空
"""
from mounth02.day01.linklist import *


class LStack:
    def __init__(self):
        self.front = self.rear = Node(None)



    def push(self,val):
        self.rear.next=Node(val)
        self.rear=self.rear.next

    def enqueue(self):
        pass


ls=LStack()
ls.push(1)
ls.push(2)
ls.push(3)
print(ls.rear.val)
