class Person:
    def __init__(self, name):
        self.name=name
    def say(self):
        print('说话')

class Sdudent(Person):
    #子类若没有构造函数 使用父类的
    pass
class Teaher(Person):
    def __init__(self,age,name):
        super().__init__(name)
        self.age=age

s01=Sdudent('zs')
s01.say()
t01=Teaher(28,'ls')
print(t01.name,t01.age)