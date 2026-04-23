# dictionary means a data type in python that stores values in key-value pairs
# key should be different but values can be same
# girl variable
# same value replaces


girl = {
    "Name": "luna",
    "Age": 23,
    "Height": 5.5,
    "Weight": 65,
    "City": ["kathmandu", "Nepal"],
    "Religion": "christian",
}
print(girl)
print(type(girl))
print(len(girl))
print(girl["Name"])


# dic kun kun key xa vaneyra tahapaunu
print(girl.keys())
print(girl.values())
print(girl["City"])


# update

user_info = {"id": 1, "name": "luna", "city": "dang"}
# user_info['city']="pokhara"
# user_info['number']='1213'
# user_info['address']='nepal'
# OR
user_info.update({
    "city": "pokhara",
    "number": 232,
    "name": "ritika"
})
print(user_info)


# to remove
# 1 del  deletes all variables
# 2 pop
# 3 popitem
# 4 clear

user_info = {
    "city":"kavre",
    "name":"liyon",
    "number":589,
    "age":48,
    "height":25
}
del user_info['city']
print(user_info)



# pop
user_info.pop('number')
print(user_info)

# popitem last data remove
user_info.popitem()
print(user_info)


# clear remove all data
user_info.clear()
print(user_info)


user_info = {
    "city":"kavre",
    "name":"liyon",
    "number":589,
    "age":48,
    "height":25
}
# print(user_info['citys'])
print(user_info.get('names','not found'))




# list vitra dic rakhnu milxa mixed data

data={
    "name":"ritik",
    "phone":[
        {
        "type":"NTC",
        "num":987
        },
        {
            "type":"Ncell",
            "num":465
        }
        
    ]
}
print(data["name"],
      data["phone"][0]["type"],"number is",data["phone"][0]["num"],
      "and",
      data["phone"][1]["type"],"num is", data["phone"][1]["num"])

#  dic vitra dic

user_info = {
    "name":"hari",
    "address":{
        "tem":"lumbini",
        "per":{
            "current":"kritipur",
            "old":"kalanki"
        }
    }
}
print(user_info.keys())
print(user_info.values())
print(user_info["address"]["tem"])
print(user_info["address"]["per"]["old"])


# for loop in dic
print("----------------------------Loop---------------")
'''
for <variable> in <loop-data>:
    code block
    
for i in [1,2,3,4,5]: 
    print(i)
'''
for i in "boardways":
    print(i)
    
   
user_info = {
    "city":"kavre",
    "name":"liyon",
    "number":589,
    "age":48,
    "height":25
}
for i in user_info:
    print(i, user_info[i])
    
for i in user_info.items():
    print(i)