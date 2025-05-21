import os

# Récupérer le chemin où on se situe
current_path = os.getcwd()

with open(f'{current_path}/file.txt', 'a+') as file:
    file.seek(0) # Bouge le curseur à la ligne 0
    content = file.read(3)
    print(content)

    file.seek(0)
    for line in file: # Plus performant
        print(line.strip())

    file.write(f'On va ajouter du contenu dans {current_path}\n')
    # file.close() # Fait auto par le with

# On va faire un script qui crée un fichier
# On insère les nombres pairs de 0 à 10 dans le fichier sur chaque ligne
# Si le fichier contient déjà les nombres pairs, on ne fait rien
file = open(f'{current_path}/exercice.txt', 'a+')
file.seek(0)

end = 10

content = file.read()
current = content.strip().split('\n')
test = ['0', '2', '4', '6', '8']

if current == list(test):
    file.close()
    exit()

for i in test:
    file.write(f'{str(i)}\n')

file.close()
