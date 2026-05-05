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


# import random
# random_num = random = random.randint(0,20)
# count = 0


# while True:
#     count += 1
#     user_num = int(input("Guess the number"))
#     if user_num == random_num:
#         print(f"number guess successfully, you gussed in{count} trials")
#         break
#     else:
#         if user_num>random_num:
#             print("the number is lower")
#         else:
#             print("number is higher")
    
'''
    
import random
random_num = random.randint(0,20)
print(random_num)
count = 0
game_count= 1
 
while True:
    count += 1
    user_num = int(input("Guess the number: "))
    if user_num == random_num:
        print(f"Number Guess Successfully, You guessed in {count} trials")
        x= input("Do you want to continue? (y/n): ")
        if x.lower() == 'y':
            game_count+=1
            random_num = random.randint(0,20)
            print(random_num)
            count = 0
        else:
            print("Game Over")
            print(f"Thank you for playing with us total game= {game_count}")
            break
 
    else:
        if user_num > random_num:
            print("Too High")
        else:
            print("Too Low")
'''

import random
'''
game_count = 0

choices = ["r", "p", "s"]

while True:
    user = input("Enter r (rock), p (paper), s (scissors): ").lower()
    
    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    game_count += 1

    if user == computer:
        print("Draw")
    elif (user == "r" and computer == "s") or \
         (user == "p" and computer == "r") or \
         (user == "s" and computer == "p"):
        print("You win 🎉")
    else:
        print("Computer wins 😢")

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break

print(f"Total games played: {game_count}")
'''

'''
win condition
r => s
p => r
s => p
 
'''
while True:
    data = ["r","p","s"]
    computer = random.choice(data)
    user_num= input("Guess the r/p/s: ").lower()
    if computer == user_num:
        print("Tie")
    elif (user_num == "r" and computer == "s") or (user_num == "p" and computer == "r") or (user_num == "s" and computer == "p"):
        print("You win")
    else:
        print("Computer wins")
 