# 定义一个图形管理器类
# 1.保存所有的图形
# 2.提供计算 所有图形总面积的功能

class Tuxingguanliqi:
    def __init__(self):
        self.__tx_list=[]

    @property
    def tx_list(self):
        return self.__tx_list

    def add_tuxing(self,tx):
        self.__tx_list.append(tx)

    def zh(self):
        mianji=0
        for i in self.__tx_list:
            mianji+=i.jisuan()
        return mianji

class Tu:
    def jisuan(self):
        pass

class Yuan:
    def __init__(self,bj):
        self.bj=bj

    def jisuan(self):
        return 3.14*self.bj**2

class fang:
    def __init__(self,chang,kuan):
        self.chang=chang
        self.kuan=kuan

    def jisuan(self):
        return self.chang*self.kuan

t01=Tuxingguanliqi()
y01=Yuan(5)
f01=fang(10,15)
t01.add_tuxing(y01)
t01.add_tuxing(f01)
print(t01.zh())