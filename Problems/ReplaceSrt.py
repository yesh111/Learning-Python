name = input("Enter your name: ")
template = "Hello name! Welcome to the Python world."

if len(name) > 3:
    res =template.replace("name", name)
    print(res)
else:
    print("Name must be more than 3 characters.")
