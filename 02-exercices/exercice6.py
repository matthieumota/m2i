# Système de validation de mot de passe
password = input('Saisir un mot de passe: ')
is_valid = len(password) >= 8 and any(c.isupper() for c in password) and any(c.isnumeric() for c in password)

while not is_valid:
    print('Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule et un chiffre')
    password = input('Saisir un mot de passe: ')
    is_valid = len(password) >= 8 and any(c.isupper() for c in password) and any(c.isnumeric() for c in password)

print(f'Mot de passe valide: {password}')
