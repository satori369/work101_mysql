#技能系统
#用到封装 继承 多态
#开闭 单一 依赖倒置
#技能效果
class SkillImpactEffect:
    def impact(self):
        pass
#伤害(继承技能效果)
class DamageEffect(SkillImpactEffect):
    def __init__(self, value):
        self.value = value
    def impact(self):
        print('扣你%d血' % self.value)
# 蓝耗
class CostSPEffect(SkillImpactEffect):
    def __init__(self, value):
        self.value = value
    def impact(self):
        print('消耗%d法力' % self.value)
#降低防御力
class LoweDeffenseEffect(SkillImpactEffect):
    def __init__(self, ratio, time):
        self.ratio=ratio
        self.time=time
    def impact(self):
        print('降低防御%.1f防御力,持续%.1f秒'%self.ratio,self.time)

# 技能释放器
class SkillDeployer:
    def __init__(self,name):
        self.name = name
        #保存配置文件内容
        self.__dict_skill_config = self.__loacd_config_file()
        #b保存创建好的效果对象
        self.__list_effect_object=self.__create_effect_object()
    #读配置文件
    def __loacd_config_file(self):
        return {
            '韦坨杵':["LoweDeffenseEffect(0.3,2.5)","CostSPEffect(20)","DamageEffect(200)"],
            '亢龙有悔':["DamageEffect(500)","CostSPEffect(100)"]
        }
    #创建对象
    def __create_effect_object(self):
        list_effect_name = self.__dict_skill_config[self.name]
        return [eval(item) for item in list_effect_name]
    #调用方法
    def genernate_skill(self):
        print('看招',self.name)
        for item in self.__list_effect_object:
            print(item)
            item.impact()

skill01=SkillDeployer("亢龙有悔")
skill01.genernate_skill()

# class Shaolin(Tlianlongbabu_zhiye):
#     def __init__(self,hp,mp,ad):
#         super().__init__(hp,mp,ad)
#
#     # 少林普攻
#     def sl_pugong(self):
#         count=0
#         while True:
#             print('喝 -%d'%self.ad)
#             count+=1
#             print('看招 -%d'%self.ad)
#             count+=1
#             print('嘿 -%d'%self.ad)
#             count+=1
#             if count>=10:
#                 break
#
#     # 罗汉棍
#     def luohangun(self,mp=-10,cd=2):
#         self.mp+=mp
#         if self.mp<10:
#             print('没蓝了')
#         else:
#             print('看棍 -%d'%(self.ad*2))
#     # 摩诃无量
#     def mokewuliang(self):
#         pass
#     # 迦叶功
#     def jiayegpmg(self):
#         pass
#     # 韦陀杵
#     def weituochu(self):
#         pass
#     # 金钟罩
#     def jinzhongzhao(self):
#         pass
#     # 狮吼功
#     def shihougong(self):
#         pass
#     # 金刚伏魔
#     def jingangfumo(self):
#         pass
#
#
# s01=Shaolin(999,99,18)
# s01.sl_pugong()
# s01.luohangun()
# s01.luohangun()
# s01.luohangun()
# s01.luohangun()
# s01.luohangun()
# s01.luohangun()
# s01.luohangun()
# s01.luohangun()
#
# class Xiaoyao(Tlianlongbabu_zhiye):
#     def __init__(self, hp, mp,ad):
#         super().__init__(hp, mp,ad)
#
#     # 逍遥普攻
#     def xy_pugong(self):
#         pass
#     # 小无相功
#     def xiaoyuxianggong(self):
#         pass
#     # 祝融掌
#     def zhurongzhang(self):
#         pass
#     # 北冥神功
#     def beiminshengong(self):
#         pass
#     # 寒霜怒雪
#     def hanshaungnuxue(self):
#         pass
#     # 凌波微步
#     def lingboweibu(self):
#         pass
#     # 毁天灭地
#     def huitianmiedi(self):
#         pass
#
# class Gaibang(Tlianlongbabu_zhiye):
#     def __init__(self,hp, mp,ad):
#         super().__init__(hp, mp,ad)
#
#     # 丐帮普攻
#     def gb_pugong(self):
#         pass
#     # 飞龙在天
#     def feilongzaitian(self):
#         pass
#     # 神龙摆尾
#     def shenlongbaiwei(self):
#         pass
#     # 天下无狗
#     def tianxiawugou(self):
#         pass
#     # 醉饮江湖
#     def zuiyinjianghu(self):
#         pass
#     # 擒龙控鹤
#     def qinglongkonghe(self):
#         pass
#     # 密云不雨
#     def miyunbuyu(self):
#         pass
#     # 亢龙有悔
#     def kanglongyouhui(self):
#         pass
#
#
#
