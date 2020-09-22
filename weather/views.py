from django.shortcuts import render
import requests
from . models import City

# Create your views here.
def index(request):
    
    api="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=517b5c6002b1467aba203e80e7564ea4"
    
    cities = City.objects.all()
    weather_data = []
    
    for city in cities:
        
        r=requests.get(api.format(city)).json()
        
        city_weather = {
            'cityname': r['name'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        weather_data.append(city_weather)
        
        print(city_weather)
        
    return render(request, 'weather/index.html', context={
        "weather_data":weather_data
    })
