#老张开车去东北
class Person:
    def __init__(self, name):
        self.name=name
        self.car=Car(self.name)


    def go_to(self,position,type):
        #需要车
        #Car.run()
        print(self.name+'去'+position)
        type.run()
    # def go_to(self,position):
    #     #需要车
    #     #Car.run()
    #     print(self.name+'去'+position)
    #     self.car.run()
class Car:
    def __init__(self, owner):
        self.owner=owner

    def run(self):
        print('%s的车'%self.owner)
        print('走你~')

# c01=Car()
# lz.go_to('东北',c01)
lz=Person('老张')
ll=Person('老李')
lz.go_to('东北 ',ll.car)