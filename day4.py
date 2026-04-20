# list
a = [1, 2, 3, 4, 5, 6]
print(type(a))
print(a[0])
# print(a[9])  #index out of range

print(len(a))  # index kati aauta xa vaneyra check garna
print(a[-6])

# list can be in mixed data type
a = [1, "luna", True, 13.5]  # support mixed data type
print(a)

name = ["luna", "ritika", "saticha", "ashmita", "mamata", "anusha"]
print(name[1:5])
print(name[1:])
print(name[:6])
print(name[:])

name[1] = "luna"
print(name)

# four method to add data
# append list ko last ma data add garxa
# insert index ma data rakhxa
# extend a,b list a ko value b ma rakhne b ko value a ma rakhne existing list ma data change garne
# concat 2ota list jodeyra aarko data banune


# append
name.append("krish")
name.append("suman")
# name.append("suman","hari") aauta valu matra rakhnu milxa
print(name)
name.append([1, 2, 3, 4])  # last ma data rakhxa


# insert
name.insert(2, "insert")
print(name)

name.insert(20, "should be error")
print(name)

# extend
a = [1,2]
b = [3,4]
a.extend(b)
print(a)
print(b)
b.extend(a)
print(b)



# concat
print("....."*3)
a = [1,2]
b = [3,4]

c = a+b
print(c)
print(a,b)

# list lae hataune
# del all variable will be delete
# remove
# pop last ko data delete garxa
# clear list ko vitra ko data faldinxa

data =["luna","ritika","saticha","liyon","liyon"]
del data[1]
print(data)

# pop
deleted_name = data.pop
# data.pop(2)
print(data)
print(deleted_name)


# remove
data.remove("liyon")
data.remove("liyon")
print(data)

# clear
data.clear()
print(data)


# sort
teachers = ['luna','ritika','luna','saticha']
teachers.sort(reverse=True)
print(teachers)


data = ['Nasir', 'Irfan', 'insert', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan', 'krish', [1, 2, 3], 'should be error']
print(data[10][1])
list_data =data[10]
print(list_data[1])



# find the maximum and minimum values in a list

numbers = [12,45,7,89,23,56,3,78]
max = numbers[0]
min = numbers[0]
# in built function
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

numbers.sort()
print(numbers[0], numbers[-1])


# membership operator answer comes of true or false
# in,not in
print(1 not in numbers)
    