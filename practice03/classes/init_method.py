class A:
    def __init__(self):
        self.x = 1

class B:
    def __init__(self, x):
        self.x = x

class C:
    def __init__(self, a, b):
        self.sum = a + b

class D:
    def __init__(self, name):
        self.name = name

class E:
    def __init__(self, age=18):
        self.age = age

class F:
    def __init__(self, x):
        self.x = x

class G:
    def __init__(self):
        print("Created")

class H:
    def __init__(self, s):
        self.s = s

class I:
    def __init__(self, n):
        self.n = n

class J:
    def __init__(self, x, y):
        self.z = x * y
