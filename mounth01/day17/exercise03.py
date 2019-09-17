class Myff:
    def __init__(self, target):
        self.target=target
        self.num=-1
    def __next__(self):
        if self.num>=self.target-1:
            raise StopIteration
        self.num+=1
        return self.num



class MyRange:
    def __init__(self,r):
        self.my_range=r

    def __iter__(self):
        return Myff(self.my_range)



for item in MyRange(8888888888):
    print(item)