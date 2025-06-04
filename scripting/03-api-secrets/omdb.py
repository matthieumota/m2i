import dotenv
import math
import os
import requests
from tabulate import tabulate

def get_movie_info(title: str, api_key: str) -> dict:
    response = requests.get(f'https://www.omdbapi.com/?t={title}&apikey={api_key}')

    if response.status_code == 401:
        # raise ValueError('Erreur 401 : clé API invalide ou absente.')
        return 'Erreur 401 : clé API invalide ou absente.'

    if response.status_code != 200:
        return f'Erreur {response.status_code}'

    data = response.json()

    if data['Response'] == 'False':
        return data['Error']

    return {
        'title': data['Title'],
        'year': data['Year'],
        'director': data['Director'],
        'rating': data['imdbRating'],
    }

def search_movies(query: str, page: int, api_key: str) -> dict:
    response = requests.get(f'https://www.omdbapi.com/?s={query}&page={page}&apikey={api_key}')

    if response.status_code == 401:
        # raise ValueError('Erreur 401 : clé API invalide ou absente.')
        return 'Erreur 401 : clé API invalide ou absente.'

    if response.status_code != 200:
        return f'Erreur {response.status_code}'

    data = response.json()

    if data['Response'] == 'False':
        return data['Error']

    result = []

    for movie in data['Search']:
        result.append({
            'title': movie['Title'],
            'year': movie['Year'],
            'imdbID': movie['imdbID'],
        })

    return {
        'result': result,
        'total': math.ceil(int(data['totalResults']) / 10),
    }

dotenv.load_dotenv()

api_key = os.getenv('OMDB_API_KEY')

print(tabulate([get_movie_info('The Matrix', api_key)], headers='keys'))
print(get_movie_info('Rockie', api_key))
# print(get_movie_info('The Matrix', '123'))

result = get_movie_info('The Matrix', api_key)
assert result['title'] == 'The Matrix'

#try:
print(get_movie_info('The Matrix', '123'))
#except ValueError as e:
#    print(e)

s = input('Quel film voulez-vous rechercher ? ')
page = 1
results = []

while True:
    #try:
        search = search_movies(s, page, api_key)
        if type(search) == str:
            print(search)
            break

        results = results + search['result']
        print(tabulate(results, headers='keys'))

        print(f'\nPage {page}/{search['total']}')

        if page == search['total']:
            break

        next = input('Page suivante ? (o/n): ')

        if next == 'n':
            break

        page += 1
    #except ValueError as e:
    #    print(e)
