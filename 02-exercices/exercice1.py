# Vérifier si un nombre est positif, négatif ou nul
def input_int(prompt):
    n = input(prompt)

    if n.lstrip('-').isnumeric():
        return int(n)
    else:
        print('Veuillez entrer un nombre entier')
        return input_int(prompt)

# n = input_int('Saisir un nombre: ')

# if n > 0:
#     print('Le nombre est positif')
# elif n == 0:
#     print('Le nombre est nul')
# else:
#     print('Le nombre est négatif')

# Alternative moins lisible
# print('Le nombre est positif') if n > 0 else print('Le nombre est nul') if n == 0 else print('Le nombre est négatif')
