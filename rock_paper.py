import random

comp_num = random.randint(0, 2)
print(comp_num)

if comp_num == 2:
    print('scissors')

try:
    num = int(input('Enter your number (0 for rock, 1 for paper, 2 for scissors):\n'))
    print(f'Your number is {num}')

    if num == 0:
        print('Your choice is rock')
        if comp_num == 0:
            print("Computer's choice is rock")
            print("It's a draw")
        elif comp_num == 1:
            print("Computer's choice is paper")
            print("You lose!")
        else:
            print("Computer's choice is scissors")
            print("You won!")

    elif num == 1:
        print('Your choice is paper')
        if comp_num == 0:
            print("Computer's choice is rock")
            print("You won!")
        elif comp_num == 1:
            print("Computer's choice is paper")
            print("It's a draw")
        else:
            print("Computer's choice is scissors")
            print("You lose!")

    elif num == 2:
        print('Your choice is scissors')
        if comp_num == 0:
            print("Computer's choice is rock")
            print("You lose!")
        elif comp_num == 1:
            print("Computer's choice is paper")
            print("You won!")
        else:
            print("Computer's choice is scissors")
            print("It's a draw")

    else:
        print('Invalid choice! Please enter 0, 1, or 2.')

except ValueError:
    print("Please enter a valid number (0, 1, or 2).")