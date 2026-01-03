# Comprehension is a short and clean way to create lists, sets, or dictionaries in Python.

# Normal Way
num = []
for i in range(1,6):
    num.append(i)
    
print(num)

# List Comprehension Way
ls = [i*2 for i in range(1,6)]
print(ls)

# Dictionary Comprehension Way
ds = {i:i*i for  i in range(1,6)}
print(ds)


# Map() Applies a function to all items in a list
nums = [1, 2, 3, 4]
res = list(map(lambda x: x*2, nums))
print(res)

# Filter() filters elements based on a condition.
nums = [1, 2, 3, 4, 5]
even = list(lambda x: x%2 == 0, nums)
print(even)

# lambda is anonymous function
add = lambda a,b : a+b
print(add(5,5))

