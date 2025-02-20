import random
op=["rock","paper","scissor"]
usersel=input("Choose between rock, paper or scissor:")
computersel=random.choice(op)

print("user selected",usersel)
print("computer selected",computersel)

if usersel==computersel:
    print("Draw")
elif usersel=="rock" and computersel=="scissor":
    print("rock smashes scissor so rock wins")
elif usersel=="paper" and computersel=="rock":
    print("paper covers rock so paper wins")
elif usersel=="scissor" and computersel=="paper":
    print("scissor cuts paper so scissor wins")

else:
    print("You lose")