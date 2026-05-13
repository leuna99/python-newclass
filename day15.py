# polymorphism
'''
a ="test"
print(len(a))
a = [1,2,3,4,5,6]
print (len(a))

a = {
    "name" :"luna",
    "address":"nepal"
}
print(len(a))

'''


# file handling

# read mode
'''
f=open('games.py','r')
print(f.read())
f.close()

# write mode

f = open('git.txt','w')
f.write("this is from file handling")
f.close()
'''
# append mode
'''
f = open('git.txt','a')
f.write("this g")
f.close()
'''

with open('games.py','r') as f: #context
    print(f.read())