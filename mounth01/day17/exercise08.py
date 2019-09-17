from mounth01.day18.common.list_helper import ListHelper


class Skill:
    def __init__(self, id, name, atk, duration=None):
        self.id =id
        self.name=name
        self.atk=atk
        self.duration=duration

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

for item in ListHelper.find_ally(list01,lambda item:item.id==102):
    print(item.name)


a=ListHelper.find_allr(list01,lambda item:item.name=='九阳神功')
print(a.name,a.id)


def atkhj():
    hatk=0
    for item in list01:
        hatk+=item.atk
    return hatk

def durationhj():
    hduration=0
    for item in list01:
        hduration+=item.duration
    return hduration


def atk01(item):
    return item.atk

def atk02(item):
    return item.duration

def zhhj(iterable_target,func_condition):
    hduration=0
    for item in iterable_target:
        hduration+=func_condition(item)
    return hduration

print(zhhj(list01,atk01))