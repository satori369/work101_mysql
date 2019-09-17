# list01 = ['三丰','翠山','无忌']
# #把list01中储存的地址赋值给list02
# list02 = list01
# list01[0] = '张三丰'
# print(list02[0])

# list01 = [100,[200,300]]
# 浅拷贝
# list02 = list01.copy()
# list01[1][0] = 500
# print(list02)#list02变成500



import copy

list01 = [100,[200,300]]
#深拷贝 划清界限 拷贝前的对象和拷贝后的对象互不影响
#注意 深拷贝可能会占用大量内存
list02 = copy.deepcopy(list01)
list01[1][0] = 500
print(list02)#200不变






