class Shape:
    """docstring for Shape."""

    def __init__(self, w, l, shape):
        self.width = w
        self.len = l
        self.shape = shape

    def what_an_i(self):
        print("I am {}".format(self.shape))

class Square(Shape):
    """docstring for Square."""

    def calculate_perimeter(self):
        return self.width*2 + self.len*2

class Rectangle(Shape):
    """docstring for Square."""

    def calculate_perimeter(self):
        return self.width*2 + self.len*2

square = Square(5,5,"square")
square.what_an_i()
print(square.calculate_perimeter())

rectangle = Rectangle(5,7,"rectangle")
rectangle.what_an_i()
print(rectangle.calculate_perimeter())
