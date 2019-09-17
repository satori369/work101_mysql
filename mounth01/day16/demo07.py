#面试题:能够参与for循环的对象 必须具备什么样的条件?
list01=[10,20,15,76,22]

#原理:
#通过__iter__()获取迭代器对象
iterator=list01.__iter__()
while True:
    #如果迭代器中没有可以继续__next__的值
    #会抛出"停止迭代" 异常
    try:
        item=iterator.__next__()#StopIteration
        print(item)
    except StopIteration:
        break

# {}.__iter__()

for item in iterator:
    print(item)

# 一个迭代器只能使用一次
for item in iterator:
    print(item)