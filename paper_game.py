
import random

comp_num = random.randint(0, 2)

your_num = int(input("Enter your number (0 for rock, 1 for paper, 2 for scissors):\n"))
print(f"Your number is: {your_num}")
print(f"Computer's number is: {comp_num}")

choice = {0: 'rock', 1: 'paper', 2: 'scissors'}

print(f"You chose {choice[your_num]}, Computer chose {choice[comp_num]}.")

if your_num == comp_num:
    print("It's a draw!")
elif (your_num == 0 and comp_num == 2) or (your_num == 1 and comp_num == 0) or (your_num == 2 and comp_num == 1):
    print("You win!")
elif (your_num == 0 and comp_num == 1) or (your_num == 1 and comp_num == 2) or (your_num == 2 and comp_num == 0):
    print("You lose!")
else:
    print("Invalid choice!")










