# Challenge_01 :- Picking a Random Words And Checking Answers.

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
words_list = ["Aniket", "Tyagi", "Raju", "Nihon", "Nippon"]
chosen_word = random.choice(words_list).lower()
print(chosen_word)
word_length = len(chosen_word)
display = []
level = 6
for _ in range (word_length):
  display += "_"
print(display)
end_of_game = False
while not end_of_game:
  guess = input("Enter a letter = ").lower()
  for position in  range (word_length):
      letter = chosen_word[position]
      #print(f"Current Position: {position}\nCurrent letter: {letter}\nGuess letter {guess}")
      if letter == guess:
        display[position] = letter
  if guess not in chosen_word:
     level -= 1
     if level == 0:
        end_of_game = True
        print("you are lose")        
  print(display)
  if "_" not in display:
       end_of_game = True
       print("your are won")
  
  print(stages[level])

