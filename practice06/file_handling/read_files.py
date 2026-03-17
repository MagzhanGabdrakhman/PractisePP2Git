# 1
with open("sample.txt") as f:
    print(f.read())

# 2
with open("sample.txt") as f:
    print(f.readline())

# 3
with open("sample.txt") as f:
    print(f.readlines())

# 4
with open("sample.txt") as f:
    for line in f:
        print(line.strip())

# 5
with open("sample.txt") as f:
    print(f.read(10))

# 6
f = open("sample.txt")
print(f.read())
f.close()

# 7
with open("sample.txt") as f:
    data = f.read()
    print(len(data))

# 8
with open("sample.txt") as f:
    print("Hello" in f.read())

# 9
with open("sample.txt") as f:
    lines = f.readlines()
    print(lines[0])

# 10
with open("sample.txt") as f:
    for i, line in enumerate(f):
        print(i, line)