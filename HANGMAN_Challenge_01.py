# Challenge_01 :- Picking a Random Words And Checking Answers.

import random

# import myfiles
from hangman_art import logo
from hangman_art import stages
from hangman_words import words_list

print(logo)

#Choice Random Words

chosen_word = random.choice(words_list).lower()
print(chosen_word)

#Use "len()" function for Find a length of chosen_word.
word_length = len(chosen_word)

#Create a Empty List.
display = []
level = 6

#useing a "for_loop"
for _ in range (word_length):
  display += "_"

print(display)
end_of_game = False

while not end_of_game:
  guess = input("Enter a letter = ").lower()

  if guess in display:
     print(f"You are already Choice {guess} ")

  for position in  range (word_length):
      letter = chosen_word[position]
      #print(f"Current Position: {position}\nCurrent letter: {letter}\nGuess letter {guess}")
 
      if letter == guess:
        print("You Guess a Correct Word")
        display[position] = letter

  if guess not in chosen_word:
     level -= 1
     print(f"You guessed {guess}, that's not in the word. You lose a life.")

     if level == 0:
        end_of_game = True
        print("you are lose")        

  print(display)

  if "_" not in display:
       end_of_game = True
       print("your are won")
  
  print(stages[level])

