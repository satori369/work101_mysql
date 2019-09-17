'''
列表的基础操作
'''

#1.创建列表
#空列表
# list01 = []
# #list(可迭代对象) 使用可迭代对象快速创建列表
# list01 = list()
# print(list01)

#具有值的列表
# list02 = ['lw',18,True,[1,2,3]]
# print(list02)
# list02 = list(range(4))
# print(list02)
# list02 = list('我是小妖怪')
# print(list02)

#增加
#需要借助列表的相关函数
#追加元素 append()
list02 = list(range(4))#[0,1,2,3]
# list02.append(5)#列表末尾追加一个元素
# print(list02)

for i in range(5,8):#列表末尾添加一系列元素
    list02.append(i)
print(list02)

# list02.extend(range(4,8))#使用可迭代对象扩展列表(添加一系列元素)
# print(list02)

#insert(索引,元素) 插入 [0,1,2,3,4,5,6,7]
# list02.insert(0,10)
# print(list02)

#列表的索引和切片
# list01 = [0,1,2,3,4,5]
# print(list01[0:5])#[0,1,2,3,4]
# print(list01[::-1])#[5,4,3,2,1,0]
# print(list01[-1])
# list01[-1] = 5.0
# print(list01)
# print()


#获取列表的所有元素
# list01 = [0,1,2,3,4]
# for item in list01:
#     print(item)

# list01 = [0,1,2,3,5,4,3,2,1]
# list01.remove(4)
# print(list01)
#
# del list01[3]
# print(list01)













