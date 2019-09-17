class Student:
    def __init__(self, name, score, age):
        self.name = name
        self.age = age
        self.score = score

    def print_self(self):
        print(self.name, self.age, self.score)


list01 = [
    Student('无忌', 33, 28),
    Student('赵敏', 99, 26),
    Student('芷若', 50, 24),
]


def find01(name):
    for item in list01:
        if item.name == name:
            return item


stu01 = find01('赵敏')
print(stu01.score)
# # stu01=None
# #None.score
# if stu01:#加个if就算找不到数据也不会报错
#     print(stu01.score)


# def find02():
#     list_age = []
#     for item in list01:
#         if item.age<30:
#             list_age.append(item)
#     return list_age
#
# list_result=find02()
# for item in list_result:
#     print(item.name)
#删除所有不及格的学生
def find03():
    for item in range(len(list01)-1,-1,-1):
        if list01[item].score<60:
            del list01[item]
    return item

find03()
# print(sc.name)
for i in list01:
    print(i.name)




