class Skill:
    def __init__(self, name, dps, time, mp):
        self.name=name
        self.dps=dps
        self.time=time
        self.mp=mp

    @property
    def dps(self):
        return self.__dps

    @dps.setter
    def dps(self,value):
        if 0.1<=value<=5:
            self.__dps=value
        else:
            raise ValueError('攻击比例不在范围内')

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,value):
        if 0.1<=value<=10:
            self.__time=value
        else:
            raise ValueError('持续时间不在范围内')

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self,value):
        if 0<=value<=100:
            self.__mp=value
        else:
            raise ValueError('法力消耗不在范围内')

qwer=[
    Skill('降龙十八掌',3,2,50),
    Skill('乾坤大挪移',4,5,80),
    Skill('一阳指',0.6,0.3,0),
    Skill('金钟罩',0.1,10,60)
]

#查找降龙十八掌的技能对象
def xlsbz():
    for item in qwer:
        if item.name=='降龙十八掌':
            print(item.name,item.dps,item.time,item.mp)

xlsbz()
#查找不消耗法力的技能
def mp0():
    for item in qwer:
        if item.mp==0:
            print(item.name)

mp0()
#所有技能的名称及持续时间
def qwer_name_time():
    for item in qwer:
        print(item.name,item.time)

qwer_name_time()
#删除所有不消耗法力的技能
def mp0del():
    count=0
    for i in range(len(qwer)-1,-1,-1):
        if qwer[i].mp==0:
            del qwer[i]
            count+=1
    return count

res=mp0del()
print(res)
# for i in d01:
#     print(i.name)

#找出攻击比例最大的技能
def dpsmax():
    listmax=[]
    for item in qwer:
        listmax.append(item.dps)
    for i in qwer:
        if i.dps==max(listmax):
            print(i.name)

dpsmax()

#对技能列表按持续时间升序排序
def timesx():
    for i in range(len(qwer)-1):
        for c in range(i+1,len(qwer)):
            if qwer[i].time>qwer[c].time:
                qwer[i],qwer[c]=qwer[c],qwer[i]


timesx()
for item in qwer:
    print(item.name,item.time)