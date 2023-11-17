from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests

def index(request):
    load_dotenv()
    
    API_KEY = os.getenv('OPEN_WEATHER_API')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + API_KEY

    city = 'Berlin'
    
    city_weather = requests.get(url.format(city)).json()
    
    print(city_weather)

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather' : weather}

    return render(request, 'app/index.html', context)
