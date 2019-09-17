class Wife:
    count=0

    @classmethod
    def p_count(cls):
        print(cls.count)
    def __init__(self,name):
        self.name=name
        Wife.count +=1

f01=Wife('大乔')
f02=Wife('小乔')
f03=Wife('貂蝉')
Wife.p_count()