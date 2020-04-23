class Triangle:
    """docstring for self."""

    def __init__(self,a,b,c):
        self.sidea = a
        self.sideb = b
        self.sidec = c
        self.area = 0

    def rot(self):
        import math
        a = self.sidea
        b = self.sideb
        c = self.sidec
        self.area = math.sqrt(((a+b+c)*(a+b-c)*(a-b+c)*(b+c-a))/16)
        area = self.area
        return area


triangle = Triangle(3.00,4.00,3.00)
print(triangle.rot())
