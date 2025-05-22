def convert_temperature():
    # Définition de mes variables
    try:
        temperature = float(input('Quelle est la température ? '))
    except ValueError:
        print('Veuillez entrer un nombre entier')
        return

    source = input('Quelle est l\'unité de départ ? ')
    target = input('Quelle est l\'unité d\'arrivée ? ')

    # Définition de la logique de calcul
    result = None

    # Cas où on va de Celsius à Fahrenheit
    if source == 'C' and target == 'F':
        result = temperature * 9/5 + 32
    if source == 'F' and target == 'C':
        result = (temperature - 32) / (9/5)

    if source == 'C' and target == 'K':
        result = temperature + 273.15
    if source == 'K' and target == 'C':
        result = temperature - 273.15

    if source == 'F' and target == 'K':
        result = (temperature + 459.67) * 5/9
    if source == 'K' and target == 'F':
        result = temperature * 9/5 - 459.67

    if source in ['C', 'K', 'F'] and source == target:
        result = temperature

    # Affichage et résultat de l'algorithme
    if result:
        print(f'{result}°{target}')
    else:
        print(f'Conversion impossible de {source} vers {target}')

# Lancement du programme (fonction) à l'infini
while True:
    convert_temperature()
