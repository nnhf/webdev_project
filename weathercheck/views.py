from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
# Create your views here.


def mine(request):
    if request.method == 'POST':
        city = request.POST['city']
        API_key = 'eb21e4e2b6960b25a61c48b6234c5791'
        city_link = str(city.replace(" ", "%20"))
        res = urllib.request.urlopen(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_link}&units=metric&appid={API_key}').read()
        city = city.upper()
        data = json.loads(res)
        data = {
            "temp": str(data['main']['temp']) + '°C',
            "humidity": str(data['main']['humidity']) + '%',
            "lon": str(data['coord']['lon']),
            "lat": str(data['coord']['lat']),
            "weather": str(data['weather'][0]['description']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'data': data})
