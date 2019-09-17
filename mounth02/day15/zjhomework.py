class A(object):
    def show(self):
        print('base show')

class B(A):
    # def __init__(self):
    #     self.A=A().show()

    def show(self):
        print('derived show')
        # super(B, self).show()

# obj = B()
# obj.show()
# obj.__class__ = A
# print(dir(obj))
# obj.show()

############2
# class A(object):
#     def __init__(self,a,b):
#         self.__a = a
#         self.__b = b
#
#     def __call__(self,*args,**kwargs):
#         pass
#
#     def myprint(self):
#         print('a=',self.__a,'b=',self.__b)
#
# a1 = A(10,20)
# a1.myprint()
#
# a1(80)
# a1.myprint()
########################3
class B(object):
    def fn(self):
        print('B fn')
    def __init__(self):
        print('B INIT')

class A(object):
    def fn(self):
        print('A fn')

    def __new__(cls,a):
        print('NEW',a)
        if a > 10:
            return super(A,cls).__new__(cls)
        return B()

    def __init__(self,a):
        print('INIT',a)




# a1 = A(5)
# a1.fn()
a2 = A(20)
a2.fn()

####################4
# list1 = 3,4
# list2 = 4,6,8
# dic1 = {2:4,4:16,6:36}
# set1 = {'h','r','d'}
##################5
# 9
# 20
####################6
# class A(object):
#     def __init__(self,a,b):
#         self.a1 = a
#         self.b1 = b
#         print('init')
#
#     def mydefault(self):
#         print('default')
#
#     def fn1(self):
#         return self.mydefault()
#     def fn2(self):
#         return self.mydefault()
#     def fn3(self):
#         return self.mydefault()
#
# a1 = A(10,20)
# a1.fn1()
# a1.fn2()
# a1.fn3()
#######################7
# def fun(n):
#     a = n
#     print(n)
#     if n > 8880:
#         return
#     fun(a * n)

# fun(5)
#######################8
# def strtest1(num):
#     str='first'
#     for i in range(num):
#         str += 'x'
#     return str
#
# print(strtest1(5))

#传入参数必须为整数，否则会出错。

######################9
# def fun():
#     n = 0
#     for i in range(1,101):
#         n += 1
#         if n ==9:
#             n = 0
#             print(i)
# fun()