class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()

class C:
    def say(self):
        print("C")

class D(C):
    def say(self):
        super().say()

class E:
    def __init__(self, x):
        self.x = x

class F(E):
    def __init__(self, x):
        super().__init__(x)
