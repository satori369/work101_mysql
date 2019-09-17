# tuple01 = ()#空元组
# tuple01 = tuple()
# print(tuple01)
#
# list01 = ['a','b']
# tuple02 = tuple(list01)
# print(tuple02)
# list02 = list(tuple02)
# print(list02)
#
# tuple02 = ('a')#不是元组
# tuple02 = ('a',)#如果元组只有一个元素 必须加逗号
# print(type(tuple02))
# name,age = 'lw',16 #('lw',18)  也是元组


tuple01 = ('a','b','c','d')
print(tuple01[2])
#tuple01[2] = 'c' #元组不可变 不能赋值

for item in tuple01:
    print(item)
for i in range(len(tuple01)-1,-1,-1):
    print(tuple01[i])

#del tuple01[3] #元组不可变 不能删除

tuple01 = ([1,2],3,4)

print(tuple01[0][1])

tuple01[0][1] = 2.0 #元组无法改变 元组中的列表可以改变
print()