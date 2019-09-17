'''
两个栈实现队列
'''
from mounth02.day02.lstack import LStack


class MyQueue:
    def __init__(self):
        self.en_stack = LStack()
        self.de_stack = LStack()

    def is_empty(self):
        if self.en_stack.is_emtpy() and self.de_stack.is_emtpy():
            return True
        else:
            return False

    def enqueue(self,val):
        #先将出队栈中所有的数导入到入队栈
        while self.de_stack.is_emtpy():
            self.en_stack.push(self.de_stack.pop())
        self.en_stack.push(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Error')
        #先将入队栈中的内容导入到出队栈
        while not self.en_stack.is_emtpy():
            self.de_stack.push(self.en_stack.pop())
        return self.de_stack.pop()


q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
while not q.is_empty():
    print(q.dequeue)


