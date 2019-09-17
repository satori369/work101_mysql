class Vector1:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        return Vector1(self.x+other)

    def __radd__(self, other):
        return Vector1(self.x+other)

    def __sub__(self, other):
        return Vector1(self.x-other)

    def __rmul__(self, other):
        return Vector1(self.x * other)

    def __str__(self):
        return str(self.x)

v01=Vector1(10)
print(id(v01))
print(2+v01,id(v01))
print(v01+2)

