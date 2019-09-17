#定义一个车类
class Car:
    def __init__(self, brand, speed):
        self.brand=brand
        self.sudu=speed

    def run(self):
        print('走你')

class Ddcar(Car):
    def __init__(self, cell,brand,speed):
        super().__init__(brand,speed)
        self.cell=cell

# c01=Car()
d01=Ddcar('5000毫安','雅马哈','80km/h')
print(d01.brand,d01.speed,d01.cell)
