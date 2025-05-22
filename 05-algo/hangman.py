import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

words = ['python', 'algo', 'php']
word = words[random.randint(0, len(words) - 1)].lower()
tries = 7
guess = ['_'] * len(word) # ['_', '_', '_']

while ''.join(guess) != word and tries > 0:
    if tries < 7:
        print(HANGMANPICS[7 - tries])

    last = False

    print(f'Devinez le mot suivant (encore {tries} essais) : {''.join(guess)}')
    letter = input('Entrez une lettre: ')

    # enumerate transforme ['A', 'B', 'C'] en [(0, 'A'), (1, 'B'), (2, 'C')]
    # ['P', 'H', 'P'] => ['P', '_', 'P']
    for i, l in enumerate(word):
        if letter != "" and l == letter[0].lower():
            guess[i] = l
            last = True

    if last == False:
        tries -= 1

if tries > 0:
    print(f'Bravo ! Vous avez trouvé le mot {word}')
else:
    print(f'Vous avez perdu ! Le mot était {word}')
