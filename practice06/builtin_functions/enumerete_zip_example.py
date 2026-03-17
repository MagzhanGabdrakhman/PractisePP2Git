names = ["A","B","C"]
scores = [90,80,70]

# 1
for i, n in enumerate(names):
    print(i, n)

# 2
for n, s in zip(names, scores):
    print(n, s)

# 3
print(list(zip(names, scores)))

# 4
for i in range(len(names)):
    print(names[i], scores[i])

# 5
print(list(enumerate(names)))

# 6
for i, val in enumerate(scores):
    print(i, val)

# 7
x = "123"
print(int(x))

# 8
y = 10
print(str(y))

# 9
print(isinstance(y, int))

# 10
print(isinstance("abc", str))