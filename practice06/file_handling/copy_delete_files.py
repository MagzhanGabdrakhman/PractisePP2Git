import shutil
import os

# 1
shutil.copy("file.txt", "copy1.txt")

# 2
shutil.copy("file.txt", "copy2.txt")

# 3
if os.path.exists("copy1.txt"):
    os.remove("copy1.txt")

# 4
if os.path.exists("copy2.txt"):
    os.remove("copy2.txt")

# 5
shutil.copy("file.txt", "backup.txt")

# 6
print(os.path.exists("backup.txt"))

# 7
if os.path.isfile("file.txt"):
    print("File exists")

# 8
shutil.copy("file.txt", "temp.txt")

# 9
os.remove("temp.txt")

# 10
print("Done file operations")