# n=1000
# print((1+n)*n/2)
#
# a=0
# for i in range(1001):
#     a+=i
# print(a)
'''
sort.py 排序训练
'''
#冒泡
from mounth02.day01.linklist import Linklist
from mounth02.day02.lstack import LStack
from mounth02.day02.squeue import SQueue


def bubble(l):
    n = len(l)
    #循环n - 1 次,每次确定一个最大值
    for i in range(n - 1):
        #两两比较交换
        for j in range(n-1-i):
            if l[j] > l[j+1]:
                l[j],l[j + 1] =l[j + 1],l[j]




l = [4, 5, 7, 1, 2, 9, 6, 8,49,12,43,12,13,5,1]
l2=[]
# l.sort(reverse=True)
# bubble(l)
# print(l)
ls1=LStack()
ls2=LStack()
sq=SQueue()
#快速排序
quick_sort = lambda arrange:arrange if len(arrange) <= 1 else quick_sort([item for item in arrange[1:] if item<=arrange[0]]) + [arrange[0]] + quick_sort([item for item in arrange[1:] if item>arrange[0]])


# print(quick_sort(l))

#low: 第一个元素索引号,high:最后一个元素索引号
def quick1(l,low,high):
    x = l[low]#基准
    while low<high:
        #如果后面的数比x大 high向前走
        while l[high]> x and high > low:
            high -= 1
        l[low]=l[high] # 比x小的往前甩
        #如果前面的数比x小则low往后走
        while l[low] <= x and low < high:
            low += 1
        l[high]=l[low] # 比x大的往后甩
    l[low] = x # 将x插入最终位置
    return low # 每一轮最终基准数的确定

def quick(l:list,low:int,high:int)->None:
    if low < high:
        key = quick1(l,low,high)
        quick(l,low, key - 1)
        quick(l, key + 1,high)

quick(l,0,len(l)-1)
print(l)