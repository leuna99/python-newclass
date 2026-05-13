# multiple inheritance

class A():
    a = 10
    
class B():
    b = 100
    
# class C(A,B):
#     d = 1000
class C(B,A):
    d = 1000
print(C.__mro__)
obj = C()
print(obj.a)



class Employee():
    employee_id = 77
    employee_name = "luna"
    basic_salary = 750
    
    
class Manager():
    bonus = 5600
    
class Boss(Employee,Manager):
    def total_salary(self):
        return self.bonus + self.basic_salary
obj = Boss()
print(obj.total_salary())




class Teacher():
    teacher_name = "Luna"
    subject = "Maths"
   
    def teacher_lesson(self):
        return self.subject
   
class ContentCreator():
    channel_name = "Luna Tech"
    def upload_video(self):
        return self.channel_name + "Python class"
   
class OnlineEducator(Teacher, ContentCreator):
    def show_profile(self):
        return f"Teacher Name: {self.teacher_name}, Subject: {self.subject}, Channel Name: {self.channel_name}"
   
obj = OnlineEducator()
print(obj.show_profile())
print(obj.upload_video())



class Teacher():
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject
 
    def teacher_lesson(self):
        return self.subject
   
class ContentCreator():
    def __init__(self, channel_name):
        self.channel_name = channel_name
 
    def upload_video(self):
        return self.channel_name + "Python class"
   
class OnlineEducator(Teacher, ContentCreator):
    def __init__(self, teacher_name, subject, channel_name):
        Teacher.__init__(self, teacher_name, subject)
        ContentCreator.__init__(self, channel_name)
 
    def show_profile(self):
        return f"Teacher Name: {self.teacher_name}, Subject: {self.subject}, Channel Name: {self.channel_name}"
   
obj = OnlineEducator("Luna", "ComputerScience", "Luna Tech")
print(obj.show_profile())
print(obj.upload_video())





# Encapsulation
class Test()
# 3 access modifier
# public protected private