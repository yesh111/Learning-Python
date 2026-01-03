# Dictionary is Key-Value pair
# keys must be unique
# Mutable
student = {"name" : "John", "age" : 21, "courses" : ["Math", "CompSci"]}
print(student)
student["marks"] = 85
student.pop("age")
print(student)
print(student["courses"])
# if key is not there we ill get error
# print(student["address"])  # This will raise a KeyError
print(student.get("address"))  # This will return None
k = {'qwerty','uiop','asdfgh'}
v = [1,2,3]
dict1 = dict(zip(k,v))
print(dict1)

data = {'js':'vscode','py':['vscode','pycharm'],'java':{'code':'vscode','spring':'iij'}}
print(data)
print(data['py'][1])
print(data['java']['spring'])

