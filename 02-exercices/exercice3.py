# Vérifier si un utilisateur est majeur
from exercice1 import input_int

age = input_int('Quel est votre âge? ')

if age >= 18:
    print('Vous êtes majeur')
else:
    print('Vous avez moins de 18 ans')
