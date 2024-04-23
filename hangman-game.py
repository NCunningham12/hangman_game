import random

words = ['batman', 'python', 'coding', 'avabear', 'charlie']

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8

print("Welcome to Hangman")

while attempts > 0 and '_' in word_display:
  print("\n" + " ".join(word_display))
  guess = input("Guess a letter: \n").lower()
  if guess in chosen_word:
    for index, letter in enumerate(chosen_word):
      if letter == guess:
        word_display[index] = guess
  else:
    print("Sorry, that letter does not appear in this word \n")
    attempts -= 1
    print("You have " + str(attempts) + " guesses left!")

# Game End
if '_' not in word_display:
  print("\n\nYou guessed the word!")
  print(' '.join(word_display))
  print("You Survived!")
else:
  print("You ran out of attempts! The correct word was " + chosen_word.upper())
  print("You Lose!")
