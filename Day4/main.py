import random

pc = random.randint(0, 2)
player = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(f"You chose {player}")
print(f"Computer chose {pc}")

if pc < player:
    if pc == 0:
        if player == 2:
            print("You lose")
        else:
            print("You win")
    else:
        print("You win")
elif pc > player:
    if player == 0:
        if pc == 2:
            print("You win")
        else:
            print("You lose")
    else:
        print("You lose")
else:
    print("It's a draw.")