class Dog:
    def __init__(self,name,kinds,color):
        self.name=name
        self.kinds=kinds
        self.color=color
    def eat(self,food):
        print('%s正在吃%s'%(self.name,food))

    def run(self,speed):
        print('%s的%s正在以%skm/h的速度飞奔'%(self.color,self.kinds,speed))

#创建dog对象
#调用__init__
wangcai=Dog('汪成皓','田园犬','黄色')
wangcai.eat('骨头')
wangcai.run(40)
doudou=wangcai
doudou.eat('狗粮')
wangcai.eat('火腿肠')
doudou.name='豆豆'
wangcai.eat('排骨')

list01=[wangcai,doudou,Dog('儿子','哈士奇','灰色')]
list02 = list01
list01[2].color='白色'
list02(list02[2].color)