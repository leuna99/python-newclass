# inheritance 
# single inheritance , multilevel , multiple

# single inheritance

class Parent():
    a = 10
    b = 11
class Child(Parent):
    b = 100
    c = 10
obj = Child()
print(obj.b)
print(obj.a)



class Parent():
    a = 10
    b = 11
    def __init__(self):
        print("Parent class constructor")
    
    def add(self):
        return self.a + self.b2
    
    

    
class Child(Parent):
    def __init__(self):
        print("parent class constructor")
        Parent.__init__(self)
        super().__init__()
    
    def result(self):
        return{
            "add":self.add(),
            "a":self.a,
            "b":self.b
            
        }
        
obj = Child()
# print(obj.add())
# print(obj.result())



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def displayEmployeeInfo(self):
        print(f'Name: {self.name}')
        print(f'Salary: {self.salary}')

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def displayManagerDetails(self):
        super().displayEmployeeInfo()
        print(f'Department: {self.department}')





class Employee():
    def __init__(self, employee_id, employee_name, basic_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.basic_salary = basic_salary
        
        
    def employee_detail(self):
        return f'{self.employee_id}....'
    
    
class Manager(Employee):
    bonus = 5600
    
    def total_salary(self):
        return self.bonus + self.basic_salary
    
class Boss(Manager):
    bonus = 100
    pass
    
obj = Boss(17,"luna",1500)
print(obj.employee_detail())
print(obj.total_salary())


print(Boss.__mro__) #mro order marta heraxa



class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name


class Marks:
    def __init__(self, marks1, marks2, marks3, marks4, marks5):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.marks4 = marks4
        self.marks5 = marks5

    def total_marks(self):
        return self.marks1 + self.marks2 + self.marks3 + self.marks4 + self.marks5

    def percentage(self):
        return self.total_marks() / 5


class Result(Student, Marks):
    def __init__(self, roll_no, name, marks1, marks2, marks3, marks4, marks5):
        Student.__init__(self, roll_no, name)
        Marks.__init__(self, marks1, marks2, marks3, marks4, marks5)

    def grade(self):
        per = self.percentage()
        if per >= 80:
            return "A"
        elif per >= 60:
            return "B"
        elif per >= 40:
            return "C"
        else:
            return "Fail"

    def display(self):
        return f"""
Roll No: {self.roll_no}
Name: {self.name}
Total Marks: {self.total_marks()}
Percentage: {self.percentage()}
Grade: {self.grade()}
"""


# Object
obj = Result(1, "Luna", 80, 75, 90, 85, 70)

print(obj.display())