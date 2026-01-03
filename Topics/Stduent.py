class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
    
    
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

s1.display()
s2.display()

#Local Scope
def test():
    x = 10
    print(x)
    
test()
#Enclosing Scope
def outer():
    x = 20
    def inner():
        print(x)
    inner()
outer()
#Global Scope
y = 30

def show():
    print(y)

show()

#Built-in Scope
print(len("Hello"))
print(max([1, 2, 3]))

#global Keyword
count = 0

def increment():
    global count
    count += 1
    print(count)
increment()

#nonlocal Keyword
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)
    
outer()

#Namespace Lookup Rule (LEGB Rule) ⭐
# Python searches variable names in this order:
# L → Local
# E → Enclosing
# G → Global
# B → Built-in
x = 100

def outer():
    x = 50
    def inner():
        x = 10
        print(x)
    inner()

outer()  # 10

#Global vs Local Namespace
x = 10

def func():
    x = 20
    print(x)

func()      # 20
print(x)    # 10

#global Keyword (Namespace Control)
x = 5

def update():
    global x
    x = 20

update()
print(x)  # 20

#nonlocal Keyword (Enclosing Namespace)
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()  # 20

x = 10

def func():
    print(x)
    x = 20   # ❌ Error

func()
