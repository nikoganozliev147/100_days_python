import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
end_of_game = False
l = "_"
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
display = []

for j in chosen_word:
    display.append("_")

while end_of_game == False:
    guess = input("Guess a letter.").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
        else:
            lives -= 1
    print(display)
    if lives == 0:
        end_of_game = True
        print("You lose")
    if l in display:
        end_of_game = False
    else:
        end_of_game = True
        print("You won")
