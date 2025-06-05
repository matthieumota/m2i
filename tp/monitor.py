import datetime
from dotenv import load_dotenv
from pathlib import Path
import json
import logging
import os
import requests

load_dotenv()

API_URL = os.getenv('API_URL')
API_PASSWORD = os.getenv('API_PASSWORD')
APP_LIST = os.getenv('APP_LIST', ['fiof.io']).split(',')

# Configuration du logging
Path('logs').mkdir(exist_ok=True) # Créer le dossier s'il n'existe pas
logging.basicConfig(
    filename='logs/status.log',
    level=logging.INFO,
    format="[%(asctime)s] - %(levelname)s - %(message)s",
)

# On va chercher le token sur l'api
def fetchToken():
    username = 'fiorella'

    try:
        logging.info(f'Fetching token for {username}')
        response = requests.post(f'{API_URL}/login', json={
            'username': username,
            'password': API_PASSWORD,
        }, timeout=5)
        response.raise_for_status()

        token = response.json()['access_token']
        logging.info(f'Got token for {username}')

        return token
    except requests.exceptions.HTTPError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f'Unable to get token on API with {username}')

    exit(1)

# On va chercher le status d'une app
def getStatus(token: str, app: str = 'unknown'):
    try:
        logging.info(f'Fetching status for {app}')
        response = requests.get(f'{API_URL}/status?app={app}', headers={
            'Authorization': f'Bearer {token}'
        }, timeout=5)
        response.raise_for_status()

        data = response.json()
        logging.info(f'Got status for {app}: {data}')

        return data
    except requests.exceptions.HTTPError as e:
        logging.error(f'Error fetching status for {app}: {e}')
        return {
            'app': app,
            'status': 'ERROR',
            'error': str(e),
            'timestamp': datetime.datetime.now().timestamp()
        }

token = fetchToken()

# Création du dossier reports
Path('reports').mkdir(exist_ok=True)
report_filename = f'reports/{datetime.datetime.now().date()}.json'

if os.path.exists(report_filename):
    with open(report_filename, 'r') as f:
        try:
            results = json.load(f)
            if not isinstance(results, list):
                logging.warning(f'{report_filename} is not a JSON list')
                results = []
        except json.JSONDecodeError:
            logging.warning(f'{report_filename} is empty or not valid')
            results = []
else:
    results = []

for app in APP_LIST:
    result = getStatus(token, app)
    if result:
        results.append(result)

with open(report_filename, 'w') as f:
    json.dump(results, f, indent=2)

logging.info(f'Report saved to {report_filename}')
print(f'Report saved to {report_filename}')
