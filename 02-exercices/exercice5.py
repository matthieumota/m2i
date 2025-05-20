# Jeu de devinette

from exercice1 import input_int
import random

guess = random.randint(1, 100)
n = input_int('Devinez un nombre: ')

while n != guess:
    if n > guess:
        print('Le nombre est plus petit')
    else:
        print('Le nombre est plus grand')

    n = input_int('Devinez un nombre: ')

print(f'Bravo tu as trouvé {guess} !')
