import random
comp_num = random.randint(0,2)
your_num = int(input("enter your number(0 for rock, 1 for paper,2 for scissors )\n"))
print(f"your number is:",your_num)
print(f"computer's number is:",comp_num)
choice = {0:'rock',1:'paper',2:'scissors'}
if your_num == comp_num:
    print("it's draw")
elif (your_num == 0 and comp_num == 2) or(your_num == 1 and comp_num == 0)or (your_num == 2 and comp_num == 1):
    print('you lose')
else:
    print("invalid choice")









