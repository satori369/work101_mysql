#老张开车去东北
#需求变化" 坐飞机
#         坐火车
#         骑车
class Vehicle:
    '''
    交通工具
    '''
    def transport(self,position):
        pass


class person():
    def __init__(self, name):
        self.name=name

    def go_to(self,position,vehicle):

        print('去:'+position)
        vehicle.transport(position)

class run(Vehicle):
    def transport(self,position):
        print('开车到',position)

class feiji(Vehicle):
    def transport(self,position):
        print('坐飞机到',position)

    # def huoche(self):
    #     print('坐火车')
    # def zixingche(self):
    #     print('自行车')
c01=Vehicle()
f01=feiji()
r01=run()
lz=person('老张')
lz.go_to('东北',r01)