import dotenv
import os
import requests

dotenv.load_dotenv()

token = os.getenv('API_TOKEN')

# Connexion avec token
response = requests.get('https://httpbin.org/bearer', headers={
    'Authorization': f'Bearer {token}'
})

if response.status_code == 200:
    print(response.json())

if response.status_code == 401:
    print('Unauthorized')

user = 'fiorella'
password = os.getenv('DB_PASSWORD')

response = requests.get(f'https://httpbin.org/basic-auth/{user}/{password}', auth=(user, password))

if response.status_code == 200:
    print(response.json())
else:
    print('Unauthorized')

# Faire une requete sur https://httpbin.org/basic-auth/{user}/{passwd}
# On remplace {user} par votre nom et {passwd} par votre mot de passe
# Cette requete, il faut l'authentifier avec un httpbasic avec votre nom et votre de mot de passe
