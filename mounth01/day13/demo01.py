#继承
#财产:钱不用自己挣 但是可以花
#王位:江山不用自己打 但是可以坐
#代码:功能不是自己写的 但是可以直接用

#多个子类在概念上一致时 考虑抽象出一个父类
#多个子类中的共性提取到父类中
#从设计角度:继承先有子类 再有父类
#从编码角度:先有父类 再有子类
class Person:
    def say(self):
        print('balabala')

class Sdudent(Person):

    def study(self):
        print('学习')

class Teacher(Person):

    def teach(self):
        print('上课')

# f01=Sdudent()
# f01.say()

#python内置函数
#isinstance()判断对象是否属于一个类
#老师对象是不是老师类型<=
t01=Teacher()
print(isinstance(t01,Teacher))
#老师对象是不是属于人类型
print(isinstance(t01,Person))
print(isinstance(t01,Sdudent))

# issubclass()判断一个类是不是另一个类的子类<
print(issubclass(Teacher,Person))

# type()  ==