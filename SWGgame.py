
import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
            
    elif comp == 'w':
        if you == 's':
           return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you=='s':
            return False
            
print("Comp Turn : Snake(s) Water(w) or Gun(g)")
# random function print random number
ranadNo = random.randint(1,3)
# print(ranadNo)
if ranadNo == 1:
    comp = 's'
elif ranadNo == 2:
    comp = 'w'
    
elif ranadNo == 3:
    comp = 'g'



you =  input("Computer Turn : Snake(s) water(W) or Gun(g)?\n")

a = game(comp,you)

print(f"computer choose: {comp}")
print(f"you choose: {you}")

game(comp,you)
if a== None:
    print('its a tie *<')
elif a:
    print('you won:)')
else:
    print('u lose:(')
