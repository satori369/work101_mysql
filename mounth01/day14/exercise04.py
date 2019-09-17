class Diren:
    def __init__(self, name, hp, atk):
        self.name=name
        self.hp=hp
        self.atk=atk

    def __str__(self):
        return '%s--%d--%d'%(self.name,self.hp,self.atk)
    def __repr__(self):
        return "Diren ('%s',%d,%d)" % (self.name,self.hp,self.atk)





d01=Diren('西瓜',99,10)
print(d01)
d02=eval(repr(d01))
print(d02)
d02=Diren('南瓜',88,20)
print(d02)
print(d01)

