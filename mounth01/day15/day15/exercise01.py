#方法一
import model02
model02.my_fun()
c = model02.MyClass02(10)
print(c.a)
c.fun02()
model02.MyClass02.fun03()
#方法二
from model02 import my_fun
from model02 import MyClass02
my_fun()
c = MyClass02(10)
print(c.a)
c.fun02()
MyClass02.fun03()
#方法三
from model02 import *
my_fun()
c = MyClass02(10)
print(c.a)
c.fun02()
MyClass02.fun03()

# 将学生管理系统分为4个模块
# model.py   class xxxModel
# bll.py    class xxxController
# usl.py    class xxxView
# main.py   调用View的代码
#运行main.py  启动学生管理系统






