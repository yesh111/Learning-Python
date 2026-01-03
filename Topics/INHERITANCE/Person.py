class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)   # initialize parent attributes
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

t1 = Teacher("john", 28, "Python")
t1.display()
