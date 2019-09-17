'''
bitree.py 二叉树的实现

思路分析:
1. 使用链式存储,Node表达一个节点(值,左连接,右连接)
2.分析遍历过程
'''

#二叉树节点
from mounth02.day02.squeue import *


class Node:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树遍历
class Bitree:
    # 传入树根
    def __init__(self, root):
        self.root=root

    # 先序遍历(跟左右)
    def preOrder(self,node):
        if node is None:
            return
        print(node.val,end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历(左跟右)
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val, end=' ')
        self.inOrder(node.right)

    # 后续遍历(左右根)
    def posOrder(self,node):
        if node is None:
            return
        self.posOrder(node.right)
        self.posOrder(node.left)
        print(node.val, end=' ')

    # 层次遍历
    def levelOrder(self,node):
        sq=SQueue()
        sq.enqueue(node)
        while not sq.is_empty():
            node = sq.dequeue()
            print(node.val, end=' ')
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)

if __name__ == '__main__':
   # B F G D H I E C A
   # 构建起一个二叉树
   b= Node('B')
   f= Node('F')
   g= Node('G')
   d= Node('D',f,g)
   h= Node('H')
   i= Node('I')
   e= Node('E',h,i)
   c= Node('C',d,e)
   a= Node('A',b,c) # 树根

   bt = Bitree(a)
   bt.preOrder(bt.root)
   # bt.inOrder(bt.root)
   # bt.posOrder(bt.root)
   bt.levelOrder(bt.root)