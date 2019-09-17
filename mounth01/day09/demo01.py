# update(dict2)
# 字典记录累加
# dict={'y':1,'z':1,'x':1}
#
#
# print(dict.get('y'))

#形式参数
#位置形参
#默认形参 给形参定义默认值 实参可以不传递
#星号元组形参 *args 位置实参理论上无线
#命名关键字形参  #放在*后面  所有的参数都需要用关键字传递
#双星号字典形参 **kwargs  让关键字实参理论上无线

#实际参数
#位置实参  实参与形参的位置对应
#序列实参  参数过多 可以将参数储存到序列 用*将序列拆分然后传值  fun(*[1,2,3])
#关键字实参 实参与形参按照名字对应  可以不按顺序传递
# 字典实参 参数过多 可以将参数储存到字典 用**将字典拆分成键值对 然后传值

# def fun01(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# list01=[1,2,3]
# fun01(*list01)
# fun01(b=2,c=3,a=1)
# dict01={'a':1,'b':2,'c':3}
# fun01(**dict01)
#
# def fun02(a=0,b=0,c=0):
#     print(a)
#     print(b)
#     print(c)
#
# fun02()
# fun02(c=10)



def fun03(**kwargs):
    # print(kwargs)
    # print(**kwargs)
    for i,b in kwargs.items():
        print(i,b)


fun03(a=1,b=2,c=3)