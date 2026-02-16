# 1
def power(a, b=2):
    return a ** b
print(power(3))

# 2
print(power(3, 3))

# 3
def greet(name="Guest"):
    print("Hello", name)
greet()

# 4
greet("Ali")

# 5
def sum3(a, b, c):
    return a + b + c
print(sum3(1, 2, 3))

# 6
def repeat(word, times=2):
    print(word * times)
repeat("Hi")

# 7
repeat("Hi", 4)

# 8
def info(name, age=18):
    print(name, age)
info("Magzhan")

# 9
info("Magzhan", 17)

# 10
def area(w, h=10):
    return w * h
print(area(5))
