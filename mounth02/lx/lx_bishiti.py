# list1 = [1,2,3,4,5,6,41,1,81,2,8]
# list2 = [6,7,8,9,10]
# for i in list2:
#     list1.append(i)
#
# list1.sort()
# print(list1)


# import re
# s = 'for i in list@ ganMe ganme game tou youXi. ticj! Dice Dice list you me you list'
#
#
#
# l = re.findall('[A-Za-z]+',s)
# # print(l)
# # # d=''
# # # l=[]
# # # for i in s:
# # #     if i !=' ':L
# # #         d += i
# # #     if i==' ':
# # #         l.append(d)
# # #         d=''
# # #         continue
# # # l.append(d)
# #
# l2 = []
# for i in l:
#     if i not in l2:
#         i_stu=l.count(i)
#         print('%s出现了%s次'%(i,i_stu))
#         l2.append(i)


#由一系列键值对组成的可变散列容器。
#可迭代对象含有iter方法,迭代器是含有iter方法和next方法的对象,生成器是将输入的对象返回为一个迭代器,
#列表是可变的,元组是不可变的
# fun=lambda c: c*6
# print(fun(5))

# list = [i for i in range(1,101)]
# s = list.copy()
# while len(list)>1:
#     for i in s:
#         if i % 9 ==0:
#             print(i)
#             list.remove(i)
# print(list)