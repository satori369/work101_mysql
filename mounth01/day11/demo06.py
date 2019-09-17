class person():
    def __init__(self, name):
        self.name=name

    def go_to(self,position,type):
        '''

        :param position: 地名
        :param type: 去的方法
        :return:
        '''
        print('去:'+position)
        type.run()

class car:
    def run(self):
        print('走你~')

c01=car()
lz=person('老张')
lz.go_to('东北',c01)