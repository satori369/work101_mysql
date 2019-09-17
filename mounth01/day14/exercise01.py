class Shoulei:
    def __init__(self,atk=99):
        self.atk=atk

    def zhale(self,target):
        if not isinstance(target,Mubiao):
            raise ValueError('对象不能受伤')
        print('炸了')
        target.beizha(self.atk)


class Mubiao:
    def beizha(self,value):
        pass

class Diren(Mubiao):
    def __init__(self, hp=100):
        self.hp=hp

    def beizha(self,value):
        print('敌人被炸了')
        self.hp-=value
        if self.hp<=0:
            print('敌人死了')

class player(Mubiao):
    def __init__(self, hp=100):
        self.hp=hp

    def beizha(self,value):
        print('玩家被炸了')
        self.hp -= value
        if self.hp <= 0:print('小动物被炸了')
        self.hp -= value
        if self.hp <= 0:
            print('玩家死了')
            print('玩家死了')

class Xiaodongwu(Mubiao):
    def __init__(self, hp=100):
        self.hp=hp

    def beizha(self,value):
        print('小动物被炸了')
        self.hp -= value
        if self.hp <= 0:
            print('玩家死了')


b01=Shoulei()
d01=Diren()
b01.zhale(d01)
b01.zhale(d01)