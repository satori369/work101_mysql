from bll import GameCoreController
from model import MoveDirection


class Usl:
    def __init__(self):
        self.__gameusl=GameCoreController()

    def chansheng(self):
        self.__gameusl.generate_new_number()
        self.__gameusl.generate_new_number()
        print(self.__gameusl.game_map)

    def __draw_map(self):
        for line in self.__gameusl.game_map:
            for item in line:
                print(item, end=" ")
            print()

    def sxzy(self):
        it=input('输入wsad移动')
        self.wsad(it)

    def wsad(self,it):
        if it=='w':
            self.__gameusl.move(MoveDirection.UP)
        elif it=='s':
            self.__gameusl.move(MoveDirection.DOWN)
        elif it == 'a':
            self.__gameusl.move(MoveDirection.LEFT)
        elif it == 'd':
            self.__gameusl.move(MoveDirection.RIGHT)



    def rukou(self):
        self.chansheng()
        while True:
            self.sxzy()
            if not self.__gameusl.tiaoguo:continue
            self.__gameusl.generate_new_number()
            self.__draw_map()
            if self.__gameusl.game_over():
                print('游戏结束')
                break

if __name__ == '__main__':
    z=Usl()
    z.rukou()