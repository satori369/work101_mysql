# append 列表末尾添加一个元素
# append 列表末尾添加一个元素
# append 列表末尾添加一个元素
# append 列表末尾添加一个元素
# append 列表末尾添加一个元素
'''
列表推导式z
快速将可迭代对象变成列表
'''
# list01 = [10,1,15,5,6,7]
# #将list01中每一个数加一放到list02中
# list02 = []
# for i in list01:
#     list02.append(i+1)
# print(list02)
#
# list03 = [i+1 for i in list01]
# print(list03)


#列表推导式嵌套
list01 = [1,2,3]
list02 = [4,5,6]
# list03 =[]
# #将两个列表中所有的值分别相加 将结果保存到list03
# for item1 in list01:
#     for item2 in list02:
#         list03.append(item1+item2)

list03 = [item2+item1 for item1 in list01 for item2 in list02]
print(list03)




