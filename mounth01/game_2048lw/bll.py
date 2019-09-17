import random,copy

from model import Location, MoveDirection


class GameCoreController:
    def __init__(self):
        self.__list01 = []
        self.__list_ling = []
        self.__game_map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.tiaoguo=False
    @property
    def game_map(self):
        return self.__game_map
    # @property
    # def tiaoguo(self):
    #     return self.__tiaoguo

    def move(self, dir=MoveDirection.UP):
        # 移动前记录地图
        original_map = copy.deepcopy(self.game_map)
        if dir == MoveDirection.UP:
            self.shangyi()
        elif dir == MoveDirection.DOWN:
            self.xiayi()
        elif dir == MoveDirection.LEFT:
            self.zuoyi()
        elif dir == MoveDirection.RIGHT:
            self.youyi()
            # 移动后进行比较
        self.tiaoguo = self.game_map != original_map

    def __quling(self):
        for i in range(len(self.__list01) - 1, -1, -1):
            if self.__list01[i]==0:
                del self.__list01[i]
                self.__list01.append(0)
# 合并
    def __hebing(self):
        self.__quling()
        for i in range(len(self.__list01) - 1):
            if self.__list01[i]==self.__list01[i + 1]:
                self.__list01[i]+=self.__list01[i + 1]
                del self.__list01[i + 1]
                self.__list01.append(0)
#zuoyi
    def zuoyi(self):
        for i in self.game_map:
            self.__list01=i
            self.__hebing()

#youyi
    def youyi(self):
        for i in self.game_map:
            self.__list01 = i[::-1]
            self.__hebing()
            i[::-1]= self.__list01

#fanzhuan
    def fanzhuan(self,list01):
        for i in range(len(list01)):
            for c in range(i+1,len(list01)):
                list01[i][c],list01[c][i]=list01[c][i],list01[i][c]

# shangyi
    def shangyi(self):
        self.fanzhuan(self.game_map)
        self.zuoyi()
        self.fanzhuan(self.game_map)

#xiayi
    def xiayi(self):
        self.fanzhuan(self.game_map)
        self.youyi()
        self.fanzhuan(self.game_map)
#随机生成数字
    def suiji(self):
        return 4 if random.randint(0,10)==1 else 2

    def zhaoling(self):
        self.__list_ling.clear()
        for i in range(len(self.game_map)):
            for c in range(len(self.game_map[i])):
                if self.game_map[i][c] == 0:
                    self.__list_ling.append(Location(i, c))

    def generate_new_number(self):
        self.zhaoling()
        if len(self.__list_ling)==0:
            return
        ic = random.choice(self.__list_ling)
        self.game_map[ic.i][ic.c] = self.suiji()

    def game_over(self):
        if len(self.__list_ling)>0:
            return False

        for i in range(len(self.game_map)):
            for c in range(len(self.game_map)-1):
                if self.game_map[i][c]==self.game_map[i+1][c] or self.game_map[c][i]==self.game_map[c+1][i]:
                    return False
        return True

if __name__ == '__main__':
    b01=GameCoreController()
    b01.shangyi()
    print(b01.game_map)
    b01.generate_new_number()
    # b01.generate_new_number()
    print(b01.game_map)
    b01.generate_new_number()
    # b01.generate_new_number()
    print(b01.game_map)
