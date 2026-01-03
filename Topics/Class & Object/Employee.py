class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def increase_salary(self):
        self.salary += self.salary * (10/100)   # increase by 10%
        
e1 = Employee(101, 50000)
print("Before Increment:", e1.salary)

e1.increase_salary()
print("After Increment:", e1.salary)
