# Numeric data type
a = 1
float_num = 1.5
complex_num = 2 + 3j
print("Numeric Data Types:")
print("Integer:", a)
print("Float:", float_num)
print("Complex:", complex_num)

# Sequence data types
name = "Alice"
nums = [1,2,3,4,5]
tuple_nums = (10, 20, 30)
print("\nSequence Data Types:")
print("String:", name)
print("List:", nums)
print("Tuple:", tuple_nums)

# Set data type
s = {1,2,3,4,5}
fs = frozenset([10,20,30])
print("\nSet Data Types:")
s.add(6)
print("Set:", s)
print("Frozenset:", fs)

# Mapping data type
student = {"name": "Ram" , "age" : 20}
print("\nMapping Data Type:")
print("Dictionary:", student)

# Boolean data type
is_pass = True
print("\nBoolean Data Type:")
print("Is Pass:", is_pass)

a = 'welcome to the python world '
b = 'welcome to the python world '
print(id(a))
print(id(b))