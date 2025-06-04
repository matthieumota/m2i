import dotenv
import logging
import os
import requests

# Mettre en place la configuration du logging
logging.basicConfig(
    level=logging.INFO, # Jusque quel level on affiche les logs
    format='%(asctime)s [%(levelname)s] %(message)s Data: %(args)s', # Format des logs
    handlers=[ # Quelles sont les destinations des logs
        # logging.StreamHandler(), # Affichage dans la console
        logging.FileHandler('log.log'), # Affichage dans un fichier
    ],
)
dotenv.load_dotenv()

# On essayer d'aller chercher le token et de vérifier qu'il soit correct
# Si il n'y a pas de token, on affiche un message d'erreur
try:
    token = os.environ['API_TOKEN']
    if token == '123': # Lever une exception
        raise ValueError('Le token est pas valide')
    url = f'https://tonapi.com?token={token}'
    logging.info(url.replace(token, '***'), {'IP': '127.0.0.1'}) # Log "pas important"
except KeyError:
    logging.error('Le token n\'est pas présent')
except Exception as e:
    logging.critical('Erreur', {'e': e.args[0]})

def fetch():
    try:
        response = requests.get('https://httpbin.org/status/403')
        response.raise_for_status() # Si le code de retour est 4xx ou 5xx, lever une exception automatiquement

        # La même chose qu'en haut mais plus explicite / précise
        if response.status_code > 500 and response.status_code <= 599:
            raise Exception(f'Erreur {response.status_code} sur l\'API {response.reason}')

        if response.status_code > 400 and response.status_code <= 499:
            raise Exception(f'Erreur {response.status_code} sur l\'API {response.reason}')

        return response
    except Exception as e:
        logging.error(e.args[0]) # Le message de l'exception
        return 'Erreur sur l\'API'

print(fetch())
