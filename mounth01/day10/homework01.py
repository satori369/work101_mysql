'''
定义敌人类
数据 姓名 血量 法力 基础攻击 防御力
行为 打印数据信息

创建敌人列表（至少4个元素）画出内存图
查找叫“灭霸”的敌人  打印信息
查找所有死亡的敌人
计算所有敌人的平均攻击力
删除防御力小于10的敌人
将所有敌人攻击力增加50

玩飞机大战   抽象  数据 行为
定义Hero类
定义Enemy类
定义Bullet类
'''
class enemy:
    count=0
    result = 0
    @classmethod
    def renshu(cls):
        print(cls.count)
    def __init__(self, name, hp, mp, ad, armor,):
        self.name=name
        self.hp=hp
        self.mp=mp
        self.ad=ad
        self.armor=armor

    def print_xw(self):
        if self.name=='灭霸':
            print('%s的血量是%s,蓝量%s,基础攻击力%s,防御力为%s' % (self.name,self.hp,self.mp,self.ad,self.armor))
        elif self.name=='钢铁侠':
            print('%s抢到了无线手套'%(self.name))
        elif self.hp==0:
            print('%s死了'%(self.name))
    def pjad(self):
        for i in list01:
            enemy.result+= i.ad
            enemy.count+=1
        pjad =enemy.result/enemy.count
        print('平均攻击力是%d'%pjad)

list01=[
    enemy('灭霸',888,666,188,30),
    enemy('钢铁侠',200,66,88,8),
    enemy('绿巨人',300,50,150,60),
    enemy('女巫',0,999,18,5)
]

#
for i in list01:
    i.print_xw()
# 平均攻击力
for ii in list01:
    ii
ii.pjad()
#删除防御力小于10
def del_armor():
    for iii in range(len(list01)-1,-1,-1):
        if list01[iii].armor<10:
            del list01[iii]
    return iii

del_armor()
for i in list01:
    print('灭霸一个响指过后,还剩下%s'%i.name)
#攻击力+50

def ad50():
    for a in list01:
        a.ad += 50

ad50()
for i in list01:
    print('%s的攻击力增加到%s'%(i.name,i.ad))

