class Circle:
    """docstring for Circle."""

    def __init__(self, d):
            self.diameter = d
            self.area = 0
            print("created!")

    def rot(self,d):
        import math
        self.area = math.pi * (d/2)**2


circle = Circle(2)
print(circle.area)
circle.rot(2)
print(circle.area)
