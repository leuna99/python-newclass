# if (condition(true))
# comparison or logical

if 2 == 2:
    print("this is true condition")
    print("this is inside true condition")
else:
    print("this is else condition")


num = 1112312

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

marks = 107
if marks < 0 or marks > 100:
    print("wrong input")
elif marks >= 90:
    print("A")
# if + else = elif
# elif marks >=90 and marks<=100:
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")


marks = 100
if marks < 0 or marks > 100:
    print("wrong input")


# Nested if

age = 20
country = "Nepal"

if age > 18:
    if country == "Nepal".lower():
        print("Eligible for license")
    else:
        print("not eligible for license")
else:
    print("Minor")


# not condition

is_raining = True
if not (is_raining):
    print("you can go outside")
    
    
gender = "M"
if gender =="M":
    print("Male")
else:
    print("Female")
    
    
data = "Male" if gender == "M" else "Female"
print(data)




# nested if
num = int(input("Enter number: "))

if num > 0 and num % 2 == 0:
    print("Positive and Even")
elif num > 0:
    print("Positive and Odd")
else:
    print("Not Positive")
    
    
    
# list
a = [1,2,3,4]
a = []
a = [1,2,"hello","1",True,False]
print(type(a))

print(a[2])
# print(a[12])

print(len(a)-12)