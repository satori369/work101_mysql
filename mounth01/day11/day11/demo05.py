#读写age
class Wife:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 25<=value<=30:
            self.__age = value
        else:
            raise ValueError("我不要！")

#只读(只能获取)age
class Wife01:
    def __init__(self, name):
        self.name = name
        self.__age = 25

    @property
    def age(self):
        return self.__age

# w01 = Wife01('小乔')
# w01.age = 18

#只写age
class Wife02:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def set_age(self,value):
        if 25<=value<=30:
            self.__age = value
        else:
            raise ValueError("我不要！")

    age = property(None,set_age)

# w03 = Wife02('大桥',28)
# print(w03.age)




