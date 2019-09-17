#创建model02.py
#定义一个函数 my_fun()
#定义一个类 MyClass02
    #构造函数
    #实例方法
    #类方法 @classmethod

#创建exercise01.py 使用三种方法导入模块model02
#调用函数my_fun 创建实例 变量a 实例方法 类方法
def my_fun():
    print('我的fun')

class MyClass02:
    def __init__(self,a):
        self.a=a

    def fun02(self):
        print('这是实例fun02')

    @classmethod
    def fun03(self):
        print('这是类方法fun03')