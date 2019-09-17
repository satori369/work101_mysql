# 玩家(攻击力)攻击敌人(血量)敌人受伤(减血)可能死亡(播放动画)
# 敌人攻击玩家 玩家受伤(减血 碎屏) 可能死亡(游戏结束)
#
# 小明去银行取钱

class pk():
    def __init__(self, name, atk, hp):
        self.name=name
        self.atk=atk
        self.hp=hp

    def gongji(self,num):
        syxl = dr.hp
        for i in range(num):
            print('玩家攻击了敌人')
            syxl -= wj.atk
            if syxl>0:
                print('敌人的血量还剩下',syxl)
            else:
                print('敌人死亡')
                return


wj=pk('玩家',100,500)
dr=pk('敌人',150,888)

wj.gongji(5)

