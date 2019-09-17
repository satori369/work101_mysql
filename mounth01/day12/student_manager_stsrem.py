#sutdent_manager_system
class StudentModel:
    '''
    学生模型
    '''
    #id不需要传值 放在最后
    def __init__(self, name="", age=0, score=0,id=0):
        '''
        创建学生对象
        :param id: 编号 该学生的唯一标识
        :param name: 名字 str
        :param age: 年龄 int
        :param score: 成绩 int
        '''
        self.id=id
        self.name = name
        self.age = age
        self.score = score

class StudentManagerController:
    '''
    学生管理控制器 处理业务逻辑
    '''
    __student_id=1000
    def __init__(self):
        self.__stu_list=[]

    @property
    def stu_list(self):
        return self.__stu_list


    def add_student(self,stu):
        #为学生设置id
        stu.id= self.__generate_id()
        #将学生添加到学生列表
        self.__stu_list.append(stu)

    #生成ID
    def __generate_id(self):
         StudentManagerController.__student_id += 1
         return StudentManagerController.__student_id

    #删除学生remove_student
        #根据id删除学生
        #删除后返回结果 成功True/失败false
    def remove_student(self,id):
        '''
        根据编号来删除学生
        :param id: 学生的编号
        :return: 删除的结果
        '''
        for i in self.__stu_list:
            if i.id==id :
                self.__stu_list.remove(i)
                return True
        return False
        # raise ValueError('删除失败:id错误')

        # for i in range(len(self.__stu_list)):
        #     self.__stu_list[i].id=id
        #     del self.stu_list[i]

    #修改学生update_student
    # s01=StudentModel('lw',18,20,1001)
    def update_student(self,stu):
        for item in self.stu_list:
            if item.id==stu.id:
                item.name=stu.name
                item.age=stu.age
                item.score=stu.score
                return True
        return print('未找到对应的学员')
#测试添加学员
# managet=StudentManagerController()
# s01=StudentModel('lw',18,20)
# s02=StudentModel('zl',55,66)
# managet.add_student(s01)
# managet.add_student(s02)

#测试删除学员
# managet=StudentManagerController()
# s01=StudentModel('lw',18,20)
# s02=StudentModel('zl',55,66)
# managet.add_student(s01)
# managet.add_student(s02)
# for item in managet.stu_list:
#     print(item.id,item.name)
# print(managet.remove_student(1002))
# for item in managet.stu_list:
#     print(item.id,item.name)

#测试修改学员信息
managet=StudentManagerController()
stu02=StudentModel('lw',18,20)
managet.add_student(stu02)
# for item in managet.stu_list:
#      print(item.id,item.name,item.age,item.score)
managet.update_student(StudentModel('张三',19,40,1001))
for item in managet.stu_list:
     print(item.id,item.name,item.age,item.score)