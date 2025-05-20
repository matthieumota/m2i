# Comparer deux nombres
from exercice1 import input_int

n1 = input_int('Saisir le premier nombre: ')
n2 = input_int('Saisir le deuxieme nombre: ')

if n1 > n2:
    print(n1)
else:
    print(n2)

# Alternative moins lisible
print(n1 if n1 > n2 else n2)
