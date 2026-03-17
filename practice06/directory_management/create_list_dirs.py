import os

# 1
os.mkdir("dir1")

# 2
os.makedirs("dir2/sub", exist_ok=True)

# 3
print(os.listdir("."))

# 4
print(os.getcwd())

# 5
print(os.path.exists("dir1"))

# 6
print(os.path.isdir("dir1"))

# 7
os.rename("dir1", "dir_new")

# 8
os.rmdir("dir_new")

# 9
files = os.listdir(".")
for f in files:
    print(f)

# 10
print(len(os.listdir(".")))