from mounth01.day18.common.list_helper import ListHelper

from mounth01.day18.common.list_helper import ListHelper
class Skill:
    def __init__(self, id, name, atk, duration=None):
        self.id =id
        self.name=name
        self.atk=atk
        self.duration=duration
    def __str__(self):
        return self.duration
list01=[
    Skill(101,'乾坤大挪移',8000,30),
    Skill(102,'九阳神功',9000,10),
    Skill(103,'九阴白骨爪',500,50),
    Skill(104,'黑虎掏心',9800,5),
    Skill(105,'葵花宝典',6000,20),
]
#生成器函数/表达式 实现:
#技能列表中 查找攻击力大于8000的技能对象.
# def func_condition01(item):
#     return item.id==102

# def func_condition02(item):
#     return item.name=='九阳神功'
###########################################
# for item in ListHelper.find_ally(list01,lambda item:item.id==102):
#     print(item.name)
#
#
# a=ListHelper.find_allr(list01,lambda item:item.name=='九阳神功')
# print(a.name,a.id)

#############################################
#攻击力总和
# print(ListHelper.heji(list01,lambda item:item.atk))

#########################################

# def jimzsj():
#     for item in list01:
#         yield (item.name,item.duration)
#
#
# def jimzad():
#     for item in list01:
#         yield (item.name,item.atk)

#################################
# def ji02(item):
#     return (item.name,item.atk)
#
# for item in ListHelper.jineng(list01,lambda item:(item.name,item.duration)):
#     print(item)
# ########################################
# e02=ListHelper.get_max(list01,lambda
#     def del_by(iterable_target,func_condition):
#         for item in iterable_target:e:e.duration)
# print(e02.name)
########################################
# def e(e):
#     return e.atk
# ListHelper.get_shengxu(list01,lambda e:e.atk)
# for i in list01:
#     print(i.name)
# filter()




