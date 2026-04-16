# type validation
# true/false

# a = 1
# data = isinstance(a, int)
# print(data)


# Arithmetic +-/%**//
# comparison
# logical

# Arithmetic +-/%**//
# integer
# a = 10
# b = 2
# print(a - b)
# print(a + b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a // b)
# print(a**b)


# String only +*
# str+str (correct)
# str+int(incorrect)
# str*str)(incorrect)
# str+int(correct)

# a = "hello "
# b = "team"
# c = "1"
# print(a + " " + b + c)
# print(a*100)


# type casting
a = "hello "
b = "team "
# print(int(a)+int(b))
c = 1
print(str(a) + str(b) + str(c))


# String formatting

name = "hari"
age = 13
address = "nepal"
box_no = 3123
# print("name=",name,"and=",age,"and address is",address)
output = f"name = {name} and age = {age} and address is {address}"
print(output)


# comparison operator

# print("hari">"ram") incorrect
print(1 == 1)
# print(1==="1") in js is correct but not in python
print("hari" == "Hari")

# logical operation and or not ans true or false input also true false
a = True
b = True
print(a and b)

print(1 == 2 and "test" != "Hello")
print(1 == 2 or "test" != "Hello")
print(not (a))
# input function or input type

a=10
b=11
a=input("type(a)")
b= int(a)
print("user entered",a) 

a= int(input("enter any value"))
