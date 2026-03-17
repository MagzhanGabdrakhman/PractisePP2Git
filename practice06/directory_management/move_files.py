import shutil
import os

# 1
os.makedirs("dest", exist_ok=True)

# 2
with open("a.txt", "w") as f:
    f.write("test")

# 3
shutil.move("a.txt", "dest/a.txt")

# 4
shutil.copy("dest/a.txt", "b.txt")

# 5
shutil.move("b.txt", "dest/b.txt")

# 6
print(os.listdir("dest"))

# 7
shutil.copy("dest/a.txt", "copy.txt")

# 8
os.remove("copy.txt")

# 9
print("Move done")

# 10
print(os.path.exists("dest/a.txt"))