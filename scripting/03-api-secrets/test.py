import requests

response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=50.63&longitude=3.06&hourly=temperature_2m&forecast_days=1')

# Faire un appel sur cette URL
# Récupérer la température dans current
# Et l'afficher
'https://api.open-meteo.com/v1/forecast?latitude=50.633&longitude=3.0586&current=temperature_2m&forecast_minutely_15=96&past_minutely_15=96'

if response.status_code == 200:
    json = response.json()

    for index in range(24):
        date = json['hourly']['time'][index]
        temperature = json['hourly']['temperature_2m'][index]
        print(f'{date}: {temperature} °C')

    print(json)
else:
    print(response.headers)
    print(f'Erreur : {response.status_code}')
