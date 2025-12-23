# Slicing is used to extract part of sequence
# Reverse string
# Check prefixes or suffixes

name = "PythonProgramming"
print(name[0:6])

word = "hello"
print(word[::-1]) # sequence[start:stop:step]

email = "student@gmail.com"
if email[:7] == "student":
    print("Valid student email")
if email[14:] == ".com":
    print("Valid .com email")
    
    
nums = [10, 20, 30, 40, 50]
print(nums[1:4])

# copying list
a = [1,2,3]
b = a[:]
b.append(4)
print(a)
print(b)

data = [5, 10, 15, 20, 25]
print(data[1:-1])

t = (100, 200, 300, 400, 500)
print(t[2:])

numbers = [1,2,3,4]
print(numbers[::-1])

# Access alternate elements
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[::2])  # even index elements

# splitting Data into parts
data = [1, 2, 3, 4, 5, 6]
mid = len(data) // 2

first_half = data[:mid]
second_half = data[mid:]

print(first_half)
print(second_half)

# Palindrome
word = "madam"

if word == word[::-1]:
    print("Palindrome")

text = "Hello!"
text = text[:-1]
print(text)