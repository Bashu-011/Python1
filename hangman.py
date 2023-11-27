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
import words

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(words.word_list)
print(f"The solution is: {chosen_word}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []
for _ in chosen_word:
    display.append('_')
print(display)
endgame = False

while endgame == False:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, it's not in the letter. You loose a life")
        lives -= 1
        if lives == 0:
            endgame = True
            print("Out of lives! You loose!")

    if "_" not in display:
        endgame = True
        print("Yaay! You Win!")
    print(stages[lives])
