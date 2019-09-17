#技能系统
#用到封装 继承 多态
#开闭 单一 依赖倒置
#技能效果
class Jnxg:
    def shifang(self):
        pass

#伤害(继承技能效果)
class Shanghai(Jnxg):
    def __init__(self, value):
        self.value=value
    def shifang(self):
        print('造成%d伤害'%self.value)
# 蓝耗
class Lanhao(Jnxg):
    def __init__(self, value):
        self.value=value
    def shifang(self):
        print('消耗%d蓝耗'%self.value)
#降低防御力,持续时间
class Jianfang(Jnxg):
    def __init__(self, value,time):
        self.time=time
        self.value=value
    def shifang(self):
        print('减少%.1f防御力,持续%.1f秒'%self.value,self.time)
# 技能释放器
class Jnsfq:
    def __init__(self,name):
        self.name=name
        self.__list_pzwj=self.__dqpzwj()
        self.__list_cjdx = self.__cjdx()
    # 读配置文件
    def __dqpzwj(self):
        return {
            '韦坨杵': ["Jianfang(0.3,2.5)", "Lanhao(20)", "Shanghai(200)"],
            '亢龙有悔': ["Shanghai(500)", "Lanhao(100)"]
        }

    #创建对象
    def __cjdx(self):
        dy=self.__list_pzwj[self.name]
        return [eval(item) for item in dy]
    #调用方法
    def dyff(self):
        print(self.name)
        for item in self.__list_cjdx:
            item.shifang()

skill01=Jnsfq("亢龙有悔")
skill01.dyff()
