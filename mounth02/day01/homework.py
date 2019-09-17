# 1. 链表 每个方法熟悉 (画图)
#      2. 有两个有序链表,是有序链表
#         l1  1  6   8  9  12  18  20 ...
#         l2  1  2   5  7  8  19 ....
#         在不创建新的链表的情况下,将两个链表合并,
#         合并后的链表仍然有序
class Node:
    def __init__(self, val,next=None):
        self.val=val  #有用数据
        self.next=next#节点关系

class Linklist:
    def __init__(self):
        self.head=Node(None)

    def init_list(self,iter):
        p=self.head
        for i in iter:
            p.next=Node(i)
            p = p.next

    def show(self):
        p=self.head.next #第一个有效节点
        while p:
            print(p.val)
            p=p.next   #p 向后移动

    def appen_d(self,val):
        p = self.head
        while p.next:
            p = p.next
        p.next=Node(val)

    def get_value(self, index):
        if index < 0:
            raise IndexError('cuole')
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError('cuole')
            p = p.next
        return p.val
    #将l2合并到l1当中
    def merge(self,l1,l2):
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        # new = None
        # if l1.val<l2.val:
        #     new=l1
        #     tmp=l1.next
        #     new.next=self.paixu(tmp,l2)
        # else:
        #     new=l2
        #     tmp=l2.next
        #     new.next=self.paixu(l1,tmp)
        # return new
        p = l1.head
        q = l2.head.next
        while p.next is not None and q is not None:
            if p.next.val < q.val:
                p = p.next
            else:
                tmp = p.next
                p.next = q
                p = p.next
                q = tmp
        if p.next is None:
            p.next = q#将最后剩余的连接上


if __name__ == '__main__':
    l1=[1,6,8,9,12,18,20]
    l2=[1,2,5,7,8,19]
    link1=Linklist()
    link2=Linklist()
    link1.init_list(l1)
    link2.init_list(l2)
    # link1.show()
    # link2.show()
###########################
    # for i in range(6):
    #     link1.appen_d(link2.get_value(i))
    #
    # link1.show()
###########################
    link1.merge(link1,link2)
    link1.show()


    # merge(link1, link2)
    # link1.show()