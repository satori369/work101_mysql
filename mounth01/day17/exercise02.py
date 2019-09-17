class EmployeeIterator:
    def __init__(self, target):
        self.__target=target
        self.js=-1
    def __next__(self):
        if self.js>=len(self.__target)-1:
           raise StopIteration
        self.js += 1
        return self.__target[self.js]


class EmployeeManager:
    def __init__(self):
        self.emp_list=[]

    def add_employee(self,tj):
        self.emp_list.append(tj)

    def __iter__(self):
        return EmployeeIterator(self.emp_list)



manager= EmployeeManager()
manager.add_employee('无忌')
manager.add_employee('翠山')
manager.add_employee('三丰')

for item in manager:
    print(item.__tager)