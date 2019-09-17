
class Node:
    '''
    包含一个简单的数字作为数据
    next 构建关系
    '''
    def __init__(self, val,next=None):
        self.val=val  #有用数据
        self.next=next#节点关系

'''
1.构建节点间关系
2.在节点中储存数据
3.对单链表进行节点操作
'''
#单链表的类
class Linklist:
    """
    思路:生成对象即表示一个单链表对象
        对象调用方法可以完成对单链表的各种操作
    """
    def __init__(self):
        '''
        初始化时 创建一个无用的节点,让对象拥有该节点,以表达链表的开端
        '''
        self.head=Node(None)

    #创建链表
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
    #判断链表是否为空
    def is_empty(self):
        return self.head.next is None

    #清空链表
    def clear(self):
        self.head.next = None

    #尾部插入
    def appen_d(self,val):
        p = self.head
        while p.next:
            p = p.next
        p.next=Node(val)

    #头部插入
    def head_insert(self,val):
        node=Node(val)
        node.next=self.head.next
        self.head.next=node

    # 指定位置插入
    def insert(self, index, val):
        p = self.head
        # 将p移动到待插入位置的前一个
        for i in range(index):
            # 超出最大范围
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    #删除节点(删除第一个val值)
    def delete(self,val):
        p=self.head
        #确定p的位置(停留在待删除节点的前一个)
        while p.next and p.next.val !=val :
            p=p.next
        #分情况讨论
        if p.next is None:
            raise ValueError('cuo')
        else:
          p.next = p.next.next

    #查找节点
    def get_value(self,index):
        if index<0:
            raise IndexError('cuole')
        p=self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError('cuole')
            p=p.next
        return p.val

if __name__ == '__main__':
    link = Linklist()
    link.init_list(range(15))
    # link.insert(5,50)
    link.show()
    print(link.get_value(5))