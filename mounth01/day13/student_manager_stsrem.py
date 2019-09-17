
class StudentModel:
    def __init__(self, name="", age=0, score=0,id=0):

        self.id=id
        self.name = name
        self.age = age
        self.score = score

class StudentManagerController:

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

    def remove_student(self,id):

        for i in self.__stu_list:
            if i.id==id :
                self.__stu_list.remove(i)
                return True
        return False
        # raise ValueError('删除失败:id错误')

        # for i in range(len(self.__stu_list)):
        #     self.__stu_list[i].id=id
        #     del self.stu_list[i]

    def update_student(self,stu):
        for item in self.stu_list:
            if item.id==stu.id:
                item.name=stu.name
                item.age=stu.age
                item.score=stu.score
                return True
        return print('未找到对应的学员')

    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for c in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score>self.__stu_list[c].score:
                    self.__stu_list[i],self.__stu_list[c]=self.__stu_list[c],self.__stu_list[i]

class StudentManagerView:
    def __init__(self):
        self.__manager=StudentManagerController()

    def __display_menu(self):
        print('''+---------------------------+
| 1)添加学生信息              |
| 2)显示学生信息              |
| 3)删除学生信息              |
| 4)修改学生信息              |
| 5)按照成绩排序              |
+---------------------------+
        ''')

    def __select_menu(self):
        option = input('请输入:')
        if option=='1':
            self.__input_students()
        elif option=='2':
            self.__output_students(self.__manager.stu_list)
        elif option=='3':
            self.__delete_student()
        elif option=='4':
            self.__modify_student()
        elif option=='5':
            self.__output_student_by_socre()

    def main(self):
        '''
        界面入口
        :return:
        '''
        while True:
            self.__display_menu()
            self.__select_menu()

    # 输入学生__input_students
    def __input_students(self):
        #收集学生信息
        #要求输入 姓名 年龄 成绩
        #创建一个学生对象
        #去控制器找add_student方法
        p_name=input('输入学生姓名')
        p_age=int(input('输入学生年龄'))
        p_score=int(input('输入学生成绩'))
        stu=StudentModel(p_name,p_age,p_score)
        self.__manager.add_student(stu)

    #查询学生__output_students
    def __output_students(self,list):
        for item in list:
            print(item.name,item.age,item.score,item.id)

    # 删除学生__delete_student
    def __delete_student(self):
        pid=int(input('输入学生id删除学生'))
        if self.__manager.remove_student(pid):
            print('删除成功')
        else:
            print('删除失败')

    # 修改学生信息__modify_student
    def __modify_student(self):
        id=int(input('请输入要修改学生的编号:'))
        name=input('请输入新的学生的姓名:')
        age=int(input('请输入新的学生的年龄:'))
        score=int(input('请输入新的学生的成绩:'))
        stu=StudentModel(name,age,score,id)
        if self.__manager.update_student(stu):
            print('修改成功')
        else:
            print('修改失败')

    def __output_student_by_socre(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)



view=StudentManagerView()
view.main()






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
# managet=StudentManagerController()
# stu02=StudentModel('lw',18,20)
# managet.add_student(stu02)
# # for item in managet.stu_list:
# #      print(item.id,item.name,item.age,item.score)
# managet.update_student(StudentModel('张三',19,40,1001))
# for item in managet.stu_list:
#      print(item.id,item.name,item.age,item.score)

#测试成绩排序
# manager=StudentManagerController()
# s01=StudentModel('lw',18,88)
# s02=StudentModel('zl',55,99)
# s03=StudentModel('zll',25,60)
# manager.add_student(s01)
# manager.add_student(s02)
# manager.add_student(s03)
# manager.order_by_score()
# for i in manager.stu_list:
#     print(i.name,i.score)