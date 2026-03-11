# workflow of project:
# 1:input from User:(rock/paper/scissor) 
# 2:computer choose (randomly not conditionally)
# 3:result

import random
item_list = ["rock","paper","scissor"]
user_choice = input("enter your move: rock/paper/scissor =")
computer_choice = random.choice(item_list)

print(f"user choise = {user_choice},computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("match tie")

elif user_choice == "rock":
    if computer_choice == "paper":
        print("computer wins")
    else:
        print("you win")

elif user_choice == "paper":
    if computer_choice == "scissor":
        print("compuer wins")
    else:
        print("you win")

elif user_choice == "scissor":
    if computer_choice == "paper":
        print("you win")
    else:
        print("compuer wins")