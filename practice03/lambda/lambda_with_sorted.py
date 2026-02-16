numbers = [5, 2, 9, 1]

# 1
print(sorted(numbers))

# 2
print(sorted(numbers, reverse=True))

# 3
print(sorted(numbers, key=lambda x: -x))

students = [
    {"name": "Ali", "grade": 85},
    {"name": "Sara", "grade": 95},
    {"name": "John", "grade": 78}
]

# 4
print(sorted(students, key=lambda x: x["grade"]))

# 5
print(sorted(students, key=lambda x: x["grade"], reverse=True))

# 6
print(sorted(students, key=lambda x: x["name"]))

words = ["apple", "banana", "kiwi"]

# 7
print(sorted(words, key=lambda x: len(x)))

# 8
print(sorted(words, key=lambda x: x[-1]))

# 9
print(sorted(words, key=lambda x: x[0]))

# 10
print(sorted(words, key=lambda x: x.count("a")))
