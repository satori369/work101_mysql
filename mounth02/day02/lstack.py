'''
lstack.py 栈的链式结构
重点代码

思路:
1. 源于节点存储数据,建立节点关联
2. 封装方法 入栈 出栈 栈空 栈顶元素
3. 链表的开头作为栈顶(不需要每次遍历)
'''
from mounth02.day02.sstack import SStack


class Node:
    '''
    包含一个简单的数字作为数据
    next 构建关系
    '''
    def __init__(self, val,next=None):
        self.val=val  #有用数据
        self.next=next#节点关系

#自定义异常
class StackError(Exception):
    pass


#链式栈
class LStack:
    def __init__(self):
        #标记栈顶位置
        self._top = None

    def is_emtpy(self):
        return self._top is None

    def push(self,val):
        self._top=Node(val,self._top)
        # node=Node(val)
        # node.next = self._top
        # self._top = node

    def pop(self):
        if self.is_emtpy():
            raise StackError('Stack is empty')
        else:
            a= self._top.val
            self._top = self._top.next
            return a

    def top(self):
        if self.is_emtpy():
            raise StackError('Stack is empty')
        return self._top.val

# node.next = top
# top = node
#
#
# re  top.val
# top = top.next
# ls=LStack()
# ls.push(10)
# ls.push(20)
# ls.push(30)
# print(ls.pop())
# print(ls.pop())
# print(ls.pop())
# print(ls.top())