# Tuple is an ordered collection
# it allows duplicates
# Immutable (cannot be changed)

t = (10,20,30)
print(len(t))
print(t[0])

Student = ("yeswanth", 21, "B.Tech")
print(Student)
# Student[1] = 22  # This will raise an error since tuples are immutable
print(type(Student))

tup = (23,45,67,43)
print(max(tup))
print(tup[0])
# tup[2] = 100  # This will raise an error since tuples are immutable
tupA = (2,'yesh',7.9)
print(tupA)

id, name, num = tupA
print(id)
print(name)
print(num)

tupB = (12,'ram',56,78,[1,2,3,5])
print(tupB)
tupB[4][3] = 4
print(tupB)

tuple1 = (1,2,3)
print(tuple1)
temp = list(tuple1)
temp[0] = 100
tuple1 = tuple(temp)
print(tuple1)