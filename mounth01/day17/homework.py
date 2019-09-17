# 3 创建敌人类(姓名,血量,攻击力,防御力)
#    创建敌人列表，存储若干敌人.
#    -- (1) 在敌人列表中查找所有死人
#    -- (2) 在敌人列表中查找血量最大的敌人
#    -- (3) 在敌人列表中查找所有敌人姓名与攻击力
class Enmey:
    def __init__(self, name, hp=None, atk=None, defense=None):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.defense=defense

list01=[
    Enmey('uzi', 0, 666, 666),
    Enmey('faker', 999, 999, 999),
    Enmey('smlz',0,555,555),
    Enmey('clealove',777,777,777),
]
#在敌人列表中查找所有死人
def get_e01():
    for i in list01:
        if i.hp==0:
            yield i

for i in get_e01():
    print(i.name)
#在敌人列表中查找血量最大的敌人
def get_e02():
    max=list01[0]
    for i in range(len(list01)-1):
        if max.hp<list01[i+1].hp:
            max=list01[i+1]
    return max.name

print(get_e02())

# 在敌人列表中查找所有敌人姓名与攻击力
def get_e03():
    for item in list01:
        yield (item.name,item.atk)

for i in get_e03():
    print(i)



#
# for item in list01:
#     for i in range(len(list01)-1):
#         if item[i]>item[i+1]and item[i]>item[i+2] and item[i]>item[i+3]:
#             retun i
#         elif:
#         elif: