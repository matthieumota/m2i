name = input('C\'est quoi ton nom ? ')
print('Bonjour ' + name + ' !')
print(f'Bonjour {name} !')

age = input('C\'est quoi ton âge ? ')
if age.isnumeric():
    age = int(age)
else:
    exit('Veuillez entrer un nombre entier')

print(f'Tu as {age} ans. Dans 2 ans, tu as {int(age) + 2}')

if age < 10:
    print('Vous avez moins de 10 ans')
elif age == 10:
    print('Vous avez 10 ans')
else:
    print('Vous avez plus de 10 ans')
