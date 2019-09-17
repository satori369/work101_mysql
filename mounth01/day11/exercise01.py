class enemy:
    def __init__(self, name, hp, atk):
        self.name=name
        # self.set_hp(hp)
        # self.set_atk(atk)
        # self.__atk=atk
        self.hp=hp
        self.atk=atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self,value):
        if 0<=value<=100:
            self.__hp = value
        else:
            raise ValueError('血量不在范围内')

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        if 1<=value<=50:
            self.__atk=value
        else:
            raise ValueError('攻击力不在范围内')
    # hp=property(get_hp,set_hp)
    # atk=property(get_atk,set_atk)


e01=enemy('剑魔',88,30)
# print(e01.get_hp())
# print(e01.get_atk())
print(e01.hp)
print(e01.atk)
# e02=enemy('蜘蛛',66,25)
# e03=enemy('维鲁斯',50,45)

