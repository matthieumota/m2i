fruits = ['pomme', 'banane', 'cerise']
print(fruits)
print(fruits[1])
print(fruits[-1])
print(fruits[len(fruits) - 1])

print(fruits[0:2]) # On part de l'index 0 et on en prends 2
print(fruits[1:2])
print(fruits[::2])

fruits_copy = fruits.copy()
fruits.sort()
print(fruits, fruits_copy)

fruits.pop(1) # Supprimer cerise
fruits.append('tomate')
fruits.insert(1, 'orange')
print(fruits)

your_tuple = (1,)
print(your_tuple)
print(your_tuple[0])
a, b = (1, 2)
print(a, b)
print(tuple(sorted((3, 2, 1))))

merged = [1, 2, 3] + [4, 5, 6] + list(your_tuple)
print(merged)

# Dictionnaires
person = {
    'name': 'Mota',
    'firstname': 'Fiorella',
    'age': 5,
    'cats': [
        { 'name': 'Mina' },
        { 'name': 'Bianca' },
    ],
    'skills': ['Dessiner', 'Jouer'],
    'is_healthy': False,
    True: False,
    0: 18,
    None: None,
}

# print(person['firstname'] + ' ' + person['name'])

def full_name(person: dict):
    return person.get('firstname', '') + ' ' + person.get('name')

print(full_name(person))

print(person.get('cats')[0]['name'])

for cat in person.get('cats'):
    print(cat.get('name'))

if person.get('is_healthy') == True:
    print('Tout va bien')
else:
    print(f'{full_name(person)} est malade... 🤮')

# Ne pas reproduire à la maison
print(person.get(0))
print(person.get(True))
print(person.get(None))

person.update({'firstname': 'Toto'})
person['firstname'] = 'Toto'
cats: list = person.get('cats', [])
cats.append({ 'name': 'A' })
print(person)
