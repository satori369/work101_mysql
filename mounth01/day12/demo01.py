#为孩子买一个玩具little pony
class Wanju():
    def __init__(self, name, size, color):
        self.name=name
        self.size=size
        self.color=color
        #组合
        self.vendor = Vendor()

    def sing(self):
        print('lalala')

    def speak(self):
        print('hello my name in LittlePony')





class Vendor:
    def __init__(self, email='123', phone=456, address=789):
        self.email=email
        self.phone=phone
        self.address=address


    def call(self):
        print('拨打厂家电话')

# tell01=Vendor()
#
# tell01.call()
w01=Wanju('LittlePony','little','white')

w01.vendor.call()