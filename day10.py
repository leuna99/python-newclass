# ?lamda function single line function

# data = lambda a,b : a+b

# print (data(1,2))
# data = lambda *args: [i**2 for i in args]
# print

# def data(*args):
#     result =[]


# class Person:
#     a = 10
#     b = 11


# obj = Person()
# print(obj.a)

# obj1 = Person()
# obj1.a = 77
# obj.c = 100
# print(obj1.a)
# print(obj1.c)

# obj2 = Person()
# print(obj2.a)


class Math:
    def__init__(self):
    print("im constructor")
        

    def add(self):
        return self.a + self.b

    def sub(self):
        return f'{self.a - self.b} - {self.c}'
    
    def result(self):
        
        self.c = "this is attrs from method"
        print(self.a)
        print(self.add())
        print(self.sub())
obj = Math()
print(obj.add())
obj.result()
obj.sub()
print(obj.c)

