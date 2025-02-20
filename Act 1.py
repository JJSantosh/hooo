import random
play=True
n=str(random.randint(10,20))

while play:
    guess=input("give me your best guess:\n")
    if n==guess:
        print("you guessed it right")
        break
    else:
        print("wrong guess try again")