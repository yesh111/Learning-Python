# During normal flow of execution, exceptions may occur. These exceptions can be handled using try and except blocks.try:
try:
    a = int(input("Enter number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("No error")
finally:
    print("Execution completed")


try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation finished")
