from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from decouple import config
import requests
from .models import Booking
from .utils import geocode

API_KEY = config('API_KEY')
def test_geocode(request):
    location = 'New York'
    url = f'https://geocode.search.hereapi.com/v1/geocode?apiKey={API_KEY}&q={location}'
    response = requests.request('GET', url)
    response = response.json()
    title = response.get('items')[0].get('title')
    lat = response.get('items')[0].get('position').get('lat')
    lng = response.get('items')[0].get('position').get('lng')
    print(lat, lng, title)

    return JsonResponse(response)


def near_hotels(request):
    if request.method == 'POST':
        location = request.POST['address']
        API_KEY = config('API_KEY')
        data = geocode(location)
        lat = data.get('lat')
        lng = data.get('lng')
        address = data.get('title')
        query = 'hotels, motels, lodge'
        url = f'https://discover.search.hereapi.com/v1/discover?apiKey={API_KEY}&at={lat},{lng}&q={query}&limit=5'
        map_url = f'https://image.maps.ls.hereapi.com/mia/1.6/mapview?apiKey={API_KEY}&lat={lat}&lon={lng}&vt=0&z=14'
        response = requests.request('GET', url)
        response = response.json()

        def get_hotel(index):
            title = response.get('items')[index].get('address').get('label')
            return title

        title1 = get_hotel(0)
        title2 = get_hotel(1)
        title3 = get_hotel(2)
        title4 = get_hotel(3)
        title5 = get_hotel(4)

    else:
        return render(request, 'hotels.html')

    context = {
        'response': response,
        'title1': title1,
        "title2": title2,
        'title3': title3,
        'title4': title4,
        'title5': title5,
        'lat': lat,
        'lng': lng,
        'address': address,
        'map_url': map_url,
    }

    return render(request, 'hotels.html', context)



