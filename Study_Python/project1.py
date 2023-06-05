
import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you == 'g':
            return 
    elif comp =='w':
        if you =='g':
            return False
        elif you=='s':
            return True   
    elif comp == 'g':
        if you =='s':
            return False
        elif you == 'w':
            return True
print("Comp 1 turn: Sanke(s) water(w) or gun(g)?")
randNo = random.randint(1,3)
print(randNo)
if randNo ==1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo ==3:
    comp = 'g'
you = input("Your  turn: Sanke(s) water(w) or gun(g)?")

a = gamewin(comp,you)
print(f"computer chose {comp}")
print(f"You chose {you}")
if a==None:
    print("the game is a tie !")
elif a:
    print("you win")
elif a:
    print("you loss")