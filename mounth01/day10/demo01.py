#类      类别   抽象
#水果                  狗
#类中的成员
#数据(名词)成员  颜色/重量/味道.....
#行为(动词)成员  生长/腐烂/.....



#对象    个体   具体
#香蕉/苹果/哈密瓜

#类与类行为不同  对象与对象之间数据不同

#类:抽象的概念  生活中的'类别'
#水果是类
#对象和实例:类的具体的实际例子 生活中某个类别的个体
#水果中的对象是:苹果...

# 类中包含数据成员和方法成员
'''
    类
    ↓
   对象
  ↓   ↓
数据  方法
'''

#定义了一个wife类
#类名首字母大写
class Wife:
    #数据成员
    #身高 体重 姓名
    def __init__(self,height,weight,name):
        self.height = height
        self.weight = weight
        self.name = name

    def abcd(self):
        print('%s正在唱歌'%self.name)

    def play(self,game):
        print('%s在玩%s'%(self.name,game))

    #行为成员
    #唱跳rep

    pass
#__init__构造函数 构造器
#  self   this
#自动调用_init_方法
w01 = Wife(2.2,90,'翠花')
print(w01.name)
w01.name='cuicui'
print(w01.name)
w01.abcd()
w01.play(2048)
# w02 = Wife(2.1,99,'如花return list02')
# print(w02.height)
# print(w02.weight)
# print(w02.name)


# #创建对象
# w01=Wife()
# print(w01)
# #w01的身高 为 2.2
# w01.height = 2.2
# print(w01.height)
# w01.weight = 90
# print(w01.weight)
# w01.name = '翠花'
# print(w01.name)
