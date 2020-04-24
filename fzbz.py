class FzBz():
    def __init__(self, strt, end):
        self.strt = strt
        self.end = end

    def multiple(self, num1, num2):
        for i in range(self.strt, self.end + 1):
            if i%num1 == 0 and i%num2 == 0:
                print("FizzBuzz")
            elif  i%num1 == 0 and i%num2 != 0:
                print("Fizz")
            elif  i%num1 != 0 and i%num2 == 0:
                print("Buzz")
            else:
                print(i)

fzbz = FzBz(1,100)
fzbz.multiple(3,5)
