class A:
    def m01(self):
        print('A m01')

class B(A):
    def m01(self):
        print('B m01')

    def m03(self):
        print('B m03')

class C(A):
    def m01(self):
        print('C m01')

class D(C,B):
    def m02(self):
        self.m01()
        self.m03()

d01 = D()
d01.m02()

print(D.mro())