class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
    def display_details(self):
        print("Name : ",self.name)
        print("Roll No : ",self.roll_no)
        print("Marks : ",self.marks)
        
s1 = Student("Tom",101,85)
s1.display_details()