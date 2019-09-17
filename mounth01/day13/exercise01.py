#定义狗Dog类 定义Bird类
class Dongwu:
    def shout (self):
        print('balabala')
    def eat(self):
        print('吃吃吃')

class Dog(Dongwu):
    def run(self):
        print('跑')

class Bird(Dongwu):
    def fly(self):
        print('飞')

animal=Dongwu()
bird=Bird()
dog=Dog()
print(type(dog)==Dog)
print(type(dog)==animal)