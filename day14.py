# polymorphism
"""
a ="test"
print(len(a))
a = [1,2,3,4,5,6]
print (len(a))

a = {
    "name" :"luna",
    "address":"nepal"
}
print(len(a))

"""

# file handling

# read mode
"""
f=open('games.py','r')
print(f.read())
f.close()

# write mode

f = open('git.txt','w')
f.write("this is from file handling")
f.close()
"""
# append mode
"""
f = open('git.txt','a')
f.write("this g")
f.close()
"""
"""
with open("games.py", "r") as f:  # context
    print(f.read())


import csv

with open("data.csv", "r") as f:
    data = csv.reader(f)
    for i in data:
        print(i[0])
        print(data)


import csv

data = [["name", "age", "role"], ["luna", 25, "student"]]
with open("data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerows(data)
"""


# json

import csv
import json

data = [["name", "age", "role"], ["luna", 25, "student"]]
with open("data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open("data.json", "r") as f:
    data = json.load(f)
    print(type(data))
    print(data["name"])


import json

data = {
    "Name": "Ali",
    "Age": 21,
    "Height": 6,
    "Weight": 55,
    "City": ["nepal", "kathmandu"],
    "Religion": "Muslim",
    "Name": "hari",
}

with open("data2.json", "w") as file:
    json.dump(data, file, intend=4)
