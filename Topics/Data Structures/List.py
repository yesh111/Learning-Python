# List is a ordered collection of elements
# it allows duplicates
# Mutable (can be changed)
numbers = [1, 2, 3, 4, 5] 
names = ["Alice", "Bob", "Charlie", "David"]
print(numbers)
print(names)    
nums = [1,2,3]
nums.append(4)
nums.insert(1,10)
nums.remove(2)
nums.pop # removes last element
nums.sort()
print(nums)
nums.reverse()
print(nums)
print(len(nums))
info = [ "Ram", 20, True, 5.5]
print(info)

#practice
a = [5,6,8,3,7,9]
b = [4,6,2,8,9,4]
c = ['abc','xyz','pqr']
mix = [1,'hello',3.5,True]
mix = [b,c]
print(mix[1])
combined = b+c
print(combined)
s = a.sort()
print(a)
print(b.count(4))
a.pop()
print(a)
del b[0:]
print(a)
print(min(a))

print(sum(a))