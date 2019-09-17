import model02
model02.my_fun()
a=model02.MyClass02(55)
print(a.a)
a.fun02()

model02.MyClass02.fun03()

# from model02 import my_fun,MyClass02
# my_fun()
# a=MyClass02(55)
# print(a.a)
# a.fun02()
# MyClass02.fun03()
from model02 import *
my_fun()
a=MyClass02(55)
print(a.a)
a.fun02()
MyClass02.fun03()