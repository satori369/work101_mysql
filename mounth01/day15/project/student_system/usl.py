from project.student_system.bll import StudentManagerController
from project.student_system.model import StudentModel


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