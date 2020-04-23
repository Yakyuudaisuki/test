class Square:
    """docstring for Square."""

    def __init__(self,a):
        self.sidea = a

    def calculate_perimeter(self):
        return self.sidea*4

    def change_size(self,a):
        self.sidea = self.sidea + a

square = Square(5)
print(square.calculate_perimeter())
square.change_size(1)
print(square.calculate_perimeter())
square.change_size(-2)
print(square.calculate_perimeter())
