fruits = ['pomme', 'banane', 'cerise']
print(fruits)
print(fruits[1])
print(fruits[-1])
print(fruits[len(fruits) - 1])

print(fruits[0:2]) # On pars de l'index 0 et on en prends 2
print(fruits[1:2])
print(fruits[::2])

fruits_copy = fruits.copy()
fruits.sort()
print(fruits, fruits_copy)

fruits.pop(1) # Supprimer cerise
fruits.append('tomate')
fruits.insert(1, 'orange')
print(fruits)
