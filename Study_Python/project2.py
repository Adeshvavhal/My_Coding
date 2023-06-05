import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Entre your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Entre a smaller number")
        else:
            print("you guessed it wrong! Entre a lager number")


print(f"you guessed the number im {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))