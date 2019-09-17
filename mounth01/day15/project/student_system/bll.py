
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