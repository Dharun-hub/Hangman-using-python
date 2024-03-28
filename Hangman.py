import random
import Hangman_words
word = random.choice(Hangman_words.words).lower()
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
print("Let's play hangman....\n")
print("Let's start by guessing a random word .... \n")
print(word)

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

display = []
for i in range(len(word)):
    display.append('_')
print(display)

life = 6
end_game = False

while end_game is False:
    guess = input("Guess the word by a random letter.\n").lower()
    for i in range(len(word)):
        if (word[i] == guess):
            display[i] = guess

    if '_' not in display:
        end_game = True
        print("You Won !!")

    if guess not in word:
        life -= 1
        if life == 0:
            end_game = True
            print("You lose !!!")

    print(display)
    print(stages[life])


