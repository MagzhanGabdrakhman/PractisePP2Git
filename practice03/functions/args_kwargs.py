# 1
def total(*args):
    return sum(args)
print(total(1, 2, 3))

# 2
print(total(5, 10))

# 3
def multiply(*args):
    r = 1
    for x in args:
        r *= x
    return r
print(multiply(2, 3, 4))

# 4
def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

# 5
show(name="Magzhan", age=17)

# 6
def mixed(a, *args):
    print(a, args)

# 7
mixed(1, 2, 3)

# 8
def info(**data):
    return data

# 9
print(info(city="Astana"))

# 10
def all_args(*a, **k):
    print(a, k)
all_args(1, 2, x=10)
