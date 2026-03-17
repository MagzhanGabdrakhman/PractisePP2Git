# 1
with open("file.txt", "w") as f:
    f.write("Hello\n")

# 2
with open("file.txt", "w") as f:
    f.write("Line1\nLine2\n")

# 3
with open("file.txt", "a") as f:
    f.write("Appended line\n")

# 4
lines = ["A\n", "B\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)

# 5
with open("file.txt", "w") as f:
    for i in range(5):
        f.write(str(i) + "\n")

# 6
with open("file.txt", "a") as f:
    f.write("End\n")

# 7
text = "Python"
with open("file.txt", "w") as f:
    f.write(text)

# 8
with open("file.txt", "w") as f:
    f.write("123")

# 9
with open("file.txt", "a") as f:
    f.write("\nNew")

# 10
with open("file.txt", "w") as f:
    f.write("Done")