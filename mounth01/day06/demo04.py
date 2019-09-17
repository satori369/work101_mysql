'''
字典的基础操作
'''

#创建字典
# dict01 ={}#空字典
# dict01 = dict()
# print(dict01)

#"lw":20
# 键  :值   键值对
# dict02 = {"lw":20}
# #字典中的数据以键值对的形式保存
# #多个键值对用逗号分隔
# dict02 = {'lw':20,'cc':30}
# print(dict02)
# #通过函数创建字典
# dict02 = dict([['name','lw'],('age',20)])
# print(dict02)

#添加元素
dict01 = {'name':'lw','age':20}
#如果字典中没有对应的键存在
#可以直接对不存在的键赋值 向字典中添加该键值对
# dict01['address'] = 'beijing'
# print(dict01)
#
# #修改
# #如果对已存在的键赋值 相当于修改原本键的值
# dict01['address'] = 'xian'
# print(dict01)
#
# #删除
# del dict01['address']
# print(dict01)
#
# # 查找字典中的元素
# print(dict01['name'])


print(dict01.get('name'))


# if 'name' in dict01:      #写if 相对直接查找 不会报错
#     print(dict01['name'])
# if 'address' in dict01:
#     print(dict01['address'])

#获取字典所有元素
for item in dict01:
    print(item)
for key in dict01:
    print(dict01[key])
#
for item in dict01.items():
    print(item)
for k,i in dict01.items():
    print(k)
    print(i)

#获取字典中所有的值
# for value in dict01.values():
#     print(value)

# dict01 = {(1,2,3):3,(1,2,3,4):4}
# print(dict01)
#
# dict01 = {[1,2,3]:3,[1,2,3,4]:4}# 可变类型无法通过哈希算法运算  所以字典的键都是不可变类型
# print(dict01)
