# class Wife:
#     pass
# w01=Wife()
# w01.name='赵敏'
# print(w01.name)
#
# w02=Wife()
# # print(w02.name)#报错
# #可以通过__dict__获取当前对象的所有实例变量
# print(w01.__dict__)
# print(w02.__dict__)

class Wife2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_self(self):
        print(self.name,self.age)

w01 = Wife2('灭绝师太',60)
w01.print_self()

# Wife2.print_self(w01)#不建议