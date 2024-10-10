
import string
import random
password = []
print("Welcome to the PyPassword Generator!")
# print(input("How many letters would you like in your password?"))

letters = list(string.ascii_lowercase+string.ascii_uppercase)
pasi = random.randint(1,(len(letters)-1))
for x in range(int(input("how many letters do you want in your password:\n"))):
    result = random.randint(1,(len(letters)-1))
    password.append(letters[result])
symbols = ['+','-','*','/','//','%',  '**', '==','!=','<','>','>=','<=', '=',  '+=',  '-=','*=', '/=','//=','%=','**=','&', '|',  '^','~','<<','>>','and','or','not','in','not in','is', 'is not',':', ',', '.', '(', ')','[', ']','{', '}','@', '#','\\','\'', '\"',  '->', '=>',  '_', ]
for x in range(int(input("how many symbols do you want in your password:\n"))):
    result = random.randint(1,(len(symbols)-1))
    password.append(symbols[result])
for x in range(int(input("how many numbers do you want in your password:\n"))):
    result = random.randint(0,9)
    password.append(result)
print(password)
random.shuffle(password)
print(password)

