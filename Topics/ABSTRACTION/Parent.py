class Father:
    def father_method(self):
        print("Father's method")

class Mother:
    def mother_method(self):
        print("Mother's method")

class Child(Father, Mother):
    def child_method(self):
        print("Child's method")

c = Child()
c.father_method()
c.mother_method()
c.child_method()

print(Child.mro())
