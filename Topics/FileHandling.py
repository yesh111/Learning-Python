# File Handling allows python programmer to read write update files

try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")


with open("example.txt","w") as file:
    file.write("\nHello, World!\n")
    file.write("This is a test file.\n")
    
with open("example.txt", "a") as file:
    file.write("\nNew Line Added")
    
    
try:
    with open("newfile.txt", "x") as file:
        file.write("Created successfully")
except FileExistsError:
    print("File already exists")
