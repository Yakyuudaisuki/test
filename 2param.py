class Person:
    def __init__(self, n):
        self.name = n

def equal(self,other):
    return self is other

bob = Person("Bob")
same_bob = bob

another_bob = Person("Bob")

print(equal(bob, same_bob))
print(equal(bob, another_bob))
