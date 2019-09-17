from mounth01.day16.AtkError import AtkError

class Enemy:
    def __init__(self,atk):
        self.atk=atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise AtkError('攻击力不在范围内', '0<=value<=100', 101)

if __name__ == '__main__':
    try:
        e01=Enemy(558)
    except AtkError as e:
        print(e.message,e.code,e.id)