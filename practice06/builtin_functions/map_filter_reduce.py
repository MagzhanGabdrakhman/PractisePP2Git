from functools import reduce

nums = [1,2,3,4,5]

# 1
print(list(map(lambda x: x+1, nums)))

# 2
print(list(map(lambda x: x*2, nums)))

# 3
print(list(filter(lambda x: x%2==0, nums)))

# 4
print(list(filter(lambda x: x>3, nums)))

# 5
print(reduce(lambda x,y: x+y, nums))

# 6
print(reduce(lambda x,y: x*y, nums))

# 7
strings = ["1","2"]
print(list(map(int, strings)))

# 8
print(list(map(str, nums)))

# 9
print(list(filter(lambda x: x!=3, nums)))

# 10
print(reduce(lambda x,y: x-y, nums))