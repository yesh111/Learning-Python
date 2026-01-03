# Set is Unordered collection
# it does not allow duplicates
# Mutable (can be changed)
s = {1,2,3,4,5}
print(s)
s.add(6)
s.remove(2)

a = {1,2,3}
b = {3,4,5}

print(a.union(b))
print(a.intersection(b))

set1 = {23,56,78,21,56}
print(set1)
print(21 in set1)
# wrong way to create a set
set2 = {}
print(type(set2))  # This will print <class 'dict'>
# to create set
set2 = set()
print(type(set2))  # This will print <class 'set'>
set2 = set('abcdmnop')
set3 = set('aeioupd')
print(set2)
print(set2-set3)
print(set2)

a = set("python")
b = set("yeswanth")
print(a&b)