'''
集合的基础操作
'''

#创建空集合
set01 = set()#set()空集合
print(set01)
#创建有两个元素的集合
set02 = {'a','b'}
print(set02)
#集合中不包含重复元素
set02 = set('abcabc')
print(set02)#{'a','b','c'}

#添加元素
#{'a','b','c'}
set02.add('lvze')
print(set02)
set02.add('mly')
print(set02)
#add 将一个对象放入集合
#列表是可变类型 不能放入集合（字符串、元组、数字）
# set02.add([0,1,2])#报错

# {'c', 'a', 'mly', 'lvze', 'b'}
#删除元素
set02.remove('a')
print(set02)
#如果要删除的元素不存在 报错
# set02.remove('x')#KeyError

#获取所有
for item in set02:
    print(item)



