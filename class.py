class Apple:
    def __init__(self, w, c, b):
        self.weight = w
        self.color = c
        self.brix = b
        self.mold = 0
        print("created")

    def rot(self, days, temp):
        self.mold = days*temp

apple = Apple(200, "red", 30)
print(apple.mold)
apple.rot(10,37)
print(apple.mold)
