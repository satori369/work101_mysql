class Wife:
    count=0

    @classmethod
    def print_count(cls):
        print(cls.count)
    def __init__(self,name):
        self.name=name
        Wife.count+=1


name01=Wife('111')
name01=Wife('222')
name01=Wife('333')
Wife.print_count()