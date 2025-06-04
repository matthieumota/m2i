import datetime
import dotenv
import logging
import os
import requests
import time

dotenv.load_dotenv()

now = datetime.datetime.now().strftime('%Y%m%d')
log_filename = f'log_{now}.log'

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    filename=log_filename
)

token = os.environ.get('API_TOKEN')

'''
Permet de masquer une partie d'une chaîne de caractères
'''
def hide(source: str, target: str):
    return source.replace(target, len(target) * '*')

'''
Permet de loguer une requête HTTP
'''
def log_request(url: str, headers: dict):
    headers = headers.copy()

    for header in headers:
        headers[header] = hide(headers[header], token)

    logging.info(f'HTTP request on {hide(url, token)} with headers: {headers}')

def log_response(r: requests.Response):
    logging.info(f'HTTP response from {hide(r.url, token)} with Status: {r.status_code} - Response: {hide(r.text, token)}')

def fetch_data(retries: int = 1, delay: int = 1):
    url = f'https://httpbin.org/bearer?apiKey={token}'
    headers = {'Authorization': f'Bearer {token}'}

    for attempt in range(1, retries + 1):
        log_request(f'{url} (attempt {attempt}/{retries})', headers)
        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            log_response(r)
            return r
        except requests.exceptions.HTTPError as e:
            logging.error(f'HTTP error: {hide(str(e), token)}')
        except requests.exceptions.RequestException as e:
            logging.error(f'Network error on {hide(url, token)}') # {hide(str(e), token)}

        if attempt < retries:
            logging.error(f'Retrying in {delay} seconds...')
            time.sleep(delay)
        if attempt == retries and retries > 1:
            logging.error('Max retries reached...')

fetch_data(30, 2)
