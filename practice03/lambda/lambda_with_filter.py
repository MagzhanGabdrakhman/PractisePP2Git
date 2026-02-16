numbers = [10, 15, 20, 25, 30, 35]

# 1
print(list(filter(lambda x: x % 2 == 0, numbers)))

# 2
print(list(filter(lambda x: x % 5 == 0, numbers)))

# 3
print(list(filter(lambda x: x > 20, numbers)))

# 4
print(list(filter(lambda x: x < 30, numbers)))

# 5
print(list(filter(lambda x: x != 25, numbers)))

# 6
print(list(filter(lambda x: x >= 15, numbers)))

# 7
print(list(filter(lambda x: x % 3 == 0, numbers)))

# 8
print(list(filter(lambda x: x == 20, numbers)))

# 9
print(list(filter(lambda x: x % 10 == 0, numbers)))

# 10
print(list(filter(lambda x: x > 100, numbers)))
