'''
容器对象
'''
#字符串 str()
#只能装字符 不可变序列

#列表  list()
#装任意数据类型 可变序列

#元组  tuple()
#装任意数据类型 不可变序列

#序列的通用操作
#+拼接两个序列
#*生成重复的序列
# += *= ...
# 索引 / 切片



#字典  dict()
#键必须是不可变类型 值可以为任意对象
#可变的散列对象

#集合  set()
#只能包含不可变类型 可变散列对象
#固定集合   不可变散列对象

# list1 = {1:'2' , 2:'3'}
#
# print(list1.get(2,-1))
# print(list1.get(3,-1))


# None  int  float   bool  complex
#  str字符串  list列表  tuple元组  dict字典  set集合

#可变 list  dict set
#不可变 数字 str  tuple

#and or   not --> 短路逻辑

#语句
#if
#while
#for

#函数********************************************
# def myprint():
#     global   #全局变量
#     nonlocal # 修改外层嵌套函数内的变量
#     return   #返回