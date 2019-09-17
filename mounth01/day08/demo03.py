'''
函数参数传递
形参
'''

#打印矩形 要求传递行数和列数 还有填充字符
#如果用户不传递填充字符 默认使用*
#默认形参 实参可以不传递数据 使用形参的默认值
#当实参传递数据时 会覆盖默认值
# def fun01(row,col,char='*'):
#     for r in range(row):
#         for c in range(col):
#             print(char,end=' ')
#         print()
# fun01(3,3)
# fun01(4,5,'+')
#
# def fun01(a=0,b=1,c=2):
#     print(a)
#     print(b)
#     print(c)
#
# #传参方式更灵活
# fun01()
# fun01(1,'b')
# fun01(c='bbbbbb')

#星号元组形参
#接受不定数量的实参 让形参的数量可以无限多
# def fun02(p1,p2,*args):
#     print(p1)
#     print(type(p2))
#     print(*args)
#
# fun02(1,2,3,4,5)
# fun02(1,2)

#在星号元组形参以后的形参叫做命名关键字形参
#传递实参的过程中 必须指定形参的名字
# def fun03(*args,p1='',p2):
#     print(*args)
#     print(p1)
#     print(p2)
# fun03(3,4,5,6,p2=2)

#sep是在两个值中间输出的字符串
#end是在最后一个值后面输出的字符串
# def myprint(*args,sep=' ',end ='\n',file=None):
#     print(*args,sep=sep,end=end)
#
# myprint(1,2,3,4)
# myprint(10,20,30,sep='+')

#星号以后的位置形参是命名关键字形参
#传递实参只接受关键字实参
# def fun04(*,p1=0,p2):
#     # print(*)
#     print(p1)
#     print(p2)
#
# fun04(p1=100,p2=200)
# fun04(p2=200)

#双星号字典形参 让关键字实参的数量无限
#将关键字实参的变量名作为字典的键 值作为字典中对应键的值保存
# def fun05(**kwargs):
#     print(kwargs)
#
# fun05(a=10,o=20)

#混合使用
# def fun06(a=10,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# fun06(20,30)

#定义一个函数 函数中包含位置形参,星号元组形参,默认形参,命名关键字形参和双星号字典形参
#定义一个函数 接受任意的参数 并输出结果
def fun01(a,*b,c,d='ddd',**e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

# fun01(1,c='ccc')
fun01(5,6,7,c='abc',d='789')

#定义一个函数 接受任意的参数 并输出结果
def fun08(*args,**kwargs):
    print(args)
    for k,v in kwargs.items():
        print(k,v)

fun08()
fun08(5,6,7,a=123,b='789')