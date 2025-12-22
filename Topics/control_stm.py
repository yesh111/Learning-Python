# Simple control statements in Python

print("break statement example:")
for i in range(5, 1, -1):
    if i == 3:
        break
    print(i)
    
print("\ncontinue statement example:")
for i in range(5):
    if i == 2:
        continue
    print(i)
    
print("\npass statement example:")
if True:
    pass   # to be implemented later
