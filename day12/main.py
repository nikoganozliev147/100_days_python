import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

def num_choice():
    return random.randint(1, 100)

diff = input("Choose a difficulty. Type 'easy' or 'hard':")

game_is_finished = False

if diff == "easy":
    lives = 10
else:
    lives = 5

while game_is_finished == False:
    number = num_choice()
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low. Guess again")
        lives -= 1
    elif guess > number:
        print("Too high. Guess again")
        lives -= 1
    else:
        print("You won!")
        game_is_finished = True
    if lives == 0:
        print("You lose")
        game_is_finished = True