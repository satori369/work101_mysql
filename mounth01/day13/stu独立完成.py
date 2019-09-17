# 界面视图类：负责处理界面逻辑，比如显示菜单，获取输入，显示结果等。
# 逻辑控制类：负责存储学生信息，处理业务逻辑。比如添加、删除等
# 数据模型类：定义需要处理的数据类型。比如学生信息。
class StudentModel:
    def __init__(self, name='', age=0, score=0,id=0):
        self.name=name
        self.age=age
        self.score=score
        self.id=id

class StudentManagerController:
    __stu_id=1000
    def __init__(self):
        self.__stu_list=[]

    @property
    def stu_list(self):
        return self.__stu_list

    #添加学生信息
    def tj_stu(self,stu):
        stu.id=self.student_id()
        self.stu_list.append(stu)

    #学生id递增
    def student_id(self):
        StudentManagerController.__stu_id += 1
        return self.__stu_id

    #显示学生信息
    def look_stu(self):
        for i in self.stu_list:
            print(i.name,i.age,i.score,i.id)

    #删除学生信息
    def del_stu(self,cid):
        for i in self.stu_list:
            if i.id==cid:
                self.stu_list.remove(i)
    #修改学生信息
    def xiugai(self,cid):
        for i in self.stu_list:
            if i.id==cid:
                xname=input('输入要修改的名字')
                xage=input('输入要修改的年龄')
                xscore=input('输入要修改的成绩')
                i.name=xname
                i.age=xage
                i.score=xscore

    #按成绩升序排序
    def paixu(self):
        for i in range(len(self.stu_list)):
            for c in range(i+1,len(self.stu_list)):
                if self.stu_list[c].score<self.stu_list[i].score:
                    self.stu_list[i],self.stu_list[c]=self.stu_list[c],self.stu_list[i]

class StudentManagerView:

    manager=StudentManagerController()

    def jiemian(self):
        print('''+----------------+
| 1)添加学生信息   |
| 2)显示学生信息   |
| 3)删除学生信息   |
| 4)修改学生信息   |
| 5)按成绩顺序查看 |
+----------------+
        ''')
        xz=int(input('请选择:'))
        self.xuanxiang(xz)

    def xuanxiang(self,ipt):

        if ipt==1:
            self.tian_stu()
        elif ipt==2:
            self.xs_stu()
        elif ipt==3:
            self.sc_stu()
        elif ipt==4:
            self.xg_stu()
        elif ipt==5:
            self.px_stu()

    #1
    def tian_stu(self):
        name = input('输入要添加的学生姓名')
        age = int(input('输入学生的年龄'))
        score = int(input('输入学生的成绩'))
        stu =StudentModel(name, age, score)
        self.manager.tj_stu(stu)
        self.jiemian()

    #2
    def xs_stu(self):
        self.manager.look_stu()
        self.jiemian()

    #3
    def sc_stu(self):
        cid=int(input('输入要删除的学生的id'))
        self.manager.del_stu(cid)
        self.jiemian()
    #4
    def xg_stu(self):
        cid = int(input('输入要修改的学生的id'))
        self.manager.xiugai(cid)
        self.jiemian()

    #5
    def px_stu(self):
        self.manager.paixu()
        self.manager.look_stu()
        self.jiemian()

s01=StudentManagerView()
s01.jiemian()