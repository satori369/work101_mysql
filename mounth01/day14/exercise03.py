#定义员工管理器
#管理所有的员工
#计算所有员工的工资
class YuangongManager:
    def __init__(self):
        self.__yggz=[]

    @property
    def yggz(self):
        return self.__yggz

    def add_yg(self,yg):
        self.__yggz.append(yg)

    def gzzh(self):
        tggz=0
        for item in self.__yggz:
            tggz+=item.salary()
        return tggz

#员工:程序员 底薪+项目分红
#销售 底薪+销售额*0.05
# ......
class Yuangong:
    def __init__(self,dixin=0):
        self.dixin=dixin

    def salary(self):
        raise NotImplementedError()

class Cxy(Yuangong):
    def __init__(self,dixin,fenhong):
        super().__init__(dixin)
        self.fenhong=fenhong

    def salary(self):

        return self.dixin+self.fenhong

class Cxk(Yuangong):
    def __init__(self,dixin,fenhong):
        super().__init__(dixin)
        self.fenhong=fenhong

    def salary(self):
        return



f01=YuangongManager()
c01=Cxy(3000,2000)
f01.add_yg(c01)
print(f01.gzzh())

