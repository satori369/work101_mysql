#([1,1],[2,2,2,2],[3,3])
from mounth01.day18.common.list_helper import ListHelper
from mounth01.day18.exercise01 import list01

tuple01=([1,1],[2,2,2,2],[3,3])
# max(可迭代对象，key = 函数)：根据函数获取可迭代对象的最大值。

# print(max(tuple01,key=lambda e:len(e)))
# print(ListHelper.get_max(tuple01,lambda e:len(e)))

# map（函数，可迭代对象）：使用可迭代对象中的每个元素调用函数，将返回值作为新可迭代对象元素；返回值为新可迭代对象。
# for i in map(lambda e:(e.name,e.atk,e.duration),list01):
#     print(i)

# for i in ListHelper.select(list01,lambda e:(e.name,e.atk,e.duration)):
#     print(i)

# min(可迭代对象，key = 函数)：根据函数获取可迭代对象的最小值。

# print(min(list01,key=lambda e:e.atk).name)
#
# print(ListHelper.get_min(list01,lambda e:e.atk).name)

#持续时间降序
# sorted(可迭代对象，key = 函数,reverse = bool值)：排序，返回值为排序结果。
for i in sorted(list01,key=lambda e:e.duration,reverse=True):
    print(i.duration)