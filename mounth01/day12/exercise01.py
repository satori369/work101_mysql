# 小明去银行取钱
class Person:
    def __init__(self, name, money):
        self.name=name
        self.money=money

class Bank():
    def __init__(self, money):
        self.money=money


    def draw_money(self,target,value):
        if value<=0:
            raise ValueError('value不能小于零')
            # return print('不能小于0')


        print(target.name,'在取',value,'钱')
        self.money -= value
        target.money+=value
        print('%s现在有%s钱'%(target.name,target.money))

xm=Person('小明',0)
zs=Bank(1000000)
zs.draw_money(xm,1000)
zs.draw_money(xm,-1000)
zs.draw_money(xm,1000)