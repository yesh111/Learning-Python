# sample function in Python
def sample():
    print("This is a sample function")

sample()

# function with parameters    
def greet(name):
    print("Hello", name)

greet("Ram")

# function with return value
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# function with default parameter
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(5, 3))

# function with variable-length arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result   
print(multiply(2, 3))
print(multiply(2, 3, 4, 5))

# function with keyword arguments
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
info(name="Ram", age=20, city="Delhi")
info(course="Python", duration="3 months")

# recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
    
print(factorial(5))

