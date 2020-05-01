import requests
from decouple import config


def geocode(location):
    API_KEY = config('API_KEY')
    url = f'https://geocode.search.hereapi.com/v1/geocode?apiKey={API_KEY}&q={location}'
    response = requests.request('GET', url)
    response = response.json()
    title = response.get('items')[0].get('title')
    lat = response.get('items')[0].get('position').get('lat')
    lng = response.get('items')[0].get('position').get('lng')
    data = {
        'title': title,
        'lat': lat,
        'lng': lng,
    }

    return data






