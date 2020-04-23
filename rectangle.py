class Rectangle(Shape):
    """docstring for Square."""

    def __init__(self,a,b):
        self.sidea = a
        self.sideb = b

    def calculate_perimeter(self):
        return self.sidea*2 + self.sideb*2

rectangle = Rectangle(5,2)
print(rectangle.calculate_perimeter())
