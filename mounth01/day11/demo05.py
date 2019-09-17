#读写 age
class Wife:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 25<=value<=30:
            self.__age=value
        else:
            raise ValueError('我不要!')

#只读(只能获取)age

