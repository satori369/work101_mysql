#张无忌 教 赵敏 乾坤大挪移
#赵敏 教 张无忌 化妆
#张无忌 上班 挣了 10000
#赵敏 上班 挣了 6000

# class People:
#     def __init__(self, name):
#         self.name=name
#
#     def qiankun(self):
#         print('%s教%s学会了乾坤大挪移'%(zwj.name,zm.name))
#
#     def huazhang(self):
#         print('%s教%s化妆'%(zm.name,zwj.name))
#
#     def shangban(self,value):
#         print('%s上班挣了%s'%(self.name,value))
#
#
# zwj=People('张无忌')
# zm=People('赵敏')
#
# People('3523523').qiankun()
# zm.huazhang()
#
# zwj.shangban(10000)
# zm.shangban(6000)



class People:
    def __init__(self, name):
        self.name=name

    def teach(self,other,skill):
        print(self.name,'教',other,skill)

    def work(self,value):
        print('%s上班挣了%s'%(self.name,value))


zwj=People('张无忌')
zm=People('赵敏')

zwj.teach(zm.name,'乾坤大挪移')
zm.teach(zwj.name,'化妆')

zwj.work(10000)
zm.work(6000)