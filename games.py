# python in built function
# import random


# random_num = random.randint(0, 20)
# print(random_num)


# while True:
#     user_num = input("Guess the number")
#     if user_num == str(random_num):
#         print("number gussed sucessfully")
#         break
#     else:
#         print("try again")


import random
random_num = random = random.randint(0,20)
count = 0


while True:
    count += 1
    user_num = int(input("Guess the number"))
    if user_num == random_num:
        print(f"number guess successfully, you gussed in{count} trials")
        break
    else:
        print("Try again!!!")
