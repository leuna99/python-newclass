# range 10,100 3 ota valuse dinxa start middle and end
# range(1,10,3)
# range(10,30) #by default 1 hunx
# range(10)  #end value loop lagdina or print gardina



for i in range(1,10,1):
    print(i)
    
    
    
for i in range(1,10,2):
    print(i)
print(",,,,,,,,,,,,,,,,,")
    
    
    
for i in range(10,1,-1):
    print(i)
    
print(",,,,,,,,,,,,,,,,,,,") 
# values only in integer


# even number fr, 1 to 100
for i in range(1,100,1):
    if i%2==0:
     print(i)
     
     

even = []
odd = []
for i in range(1,10,1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)




# nested for loop

for i in [1,2,3]:
    for j in [4,5,6,7]:
        print(i,j)
        
        
print(",,,,,,,,,,,,,,,,,,,,,,,,,,")

  
# break, continue
for i in range(1,10,1):
    if i == 5:
        break
    print(i)
    
    
    
    
# continue
for i in range(1,10,1):
    if i == 5:
        continue
    print(i)
    
    
# python mix data type list   len must be 20


my_list= [
1, "a", 2, "b", 3, "c", 4, "d", 5, "e",
6, "f", 7, "g", 8, "h", 9, "i", 10, "j"
]
for i in my_list:
    if not isinstance(i, int):
        continue
    print(i)
    
    
# for loop with else


# mostly not used
for i in range(100,1):
    print(i)
else:
    print("loop completed")
    

# for pass

for i in range (1,10,1):
    pass
# or
for i in range(1,10,1):...


# unstopable
print("-------While-----------")

# while(True):
#     print("This is true")


i = 1
while(i<10):
    print(i)
    i = i+1
    


# countdown output 
import time
i = 10
while(i<0):
    print(i)
    time.sleep(2)
    i = i-1
    
    
    
# random libary

