#面向对象三大特征
#封装
    #语法:
        #数据:一个类包装多个变量
        #行为:提供必要的功能 隐藏实现的细节
    #设计:分而治之 变而疏之
#继承
    #语法:子类拥有父类的所有成员
    #设计:隔离变化
#多态
    #语法:重写(子覆盖父类)
    #做法:父类 创建子类对象 重写-->调用父执行子
    #设计:做

#类与类的关系:
    #组合(实例变量)/泛化(继承)/依赖(参数)
    #组合链接变化和不变化的代码###
    #继承统一所有的变化###

#面向对象的设计原则:
    #开闭原则:允许增加,不允许修改
    #单一职责:一个变化
    #依赖倒置:调用父类,不调子类
    #组合复用:通过变量(参数/实例变量)调用而不是使用继承
    #里氏替换:扩展重写
    #迪米特法则:低耦合


# 功能拆分开---单一职责
dict={
            '韦坨杵': ["jianfang(0.3,2.5)", "lanhao(20)", "shanghai(200)"],
            '亢龙有悔': ["shanghai(500)", "lanhao(100)"]
        }


print(dict['亢龙有悔'])
for i in dict['亢龙有悔']:
    print(i)