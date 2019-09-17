'''
lqueuepy 链式队列
重点代码

思路分析:
1. 基于链表构建队列模型
2. 链表的头作为队头,尾作为队尾
3.定义两个标记标记队头和队尾
4.
'''
class Node:
    def __init__(self, val,next=None):
        self.val=val
        self.next=next

#自定义异常
class QueueError(Exception):
    pass

class LQueue:
    def __init__(self):
        self.front= self.rear =Node(None)

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self,val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            raise QueueError('Queue is empty')
        #front 是指向队头节点的前一个
        self.front=self.front.next
        return self.front.val


if __name__ == '__main__':
    lq=LQueue()
    for i in range(15):
        lq.enqueue(i)

    while not lq.is_empty():
        print(lq.dequeue())

