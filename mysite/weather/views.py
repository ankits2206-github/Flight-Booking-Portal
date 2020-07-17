from django.shortcuts import render
from django.contrib import messages
import requests

def weather(request):

    if request.method=='POST':
        city = request.POST['city']
        url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=yourapikey&units=metric'

        source = requests.get(url).json()

        #print(source)

        if len(source)>=10:


            tmp = float(source['main']['temp'])

            tmp=str(tmp)
            tmp=tmp+" C"
            fl=float(source['main']['feels_like'])

            fl=str(fl)+' C'
            city_weather = {
                'city': city,
                'country_code': source['sys']['country'],
                'temperature': tmp,
                'longitude' : source['coord']['lon'],
                'latitude' : source['coord']['lat'],
                'feels_like': fl,
                'humidity': source['main']['humidity'],
                'pressure': source['main']['pressure'],
                'description': source['weather'][0]['description'],
                'icon': source['weather'][0]['icon'],
                        }

            return render(request, 'weather/index.html', city_weather)

        else:
            city_weather = {
                'city': "No-info",
                'country_code': '--',
                'temperature': '--',
                'longitude': '--',
                'latitude': '--',
                'feels_like': '--',
                'humidity': '--',
                'pressure':'--',
                'description': '--',
                'icon': '',
            }
            messages.info(request, 'City Name Does not exist')
            return render(request,'weather/index.html',city_weather)
    else:
        city_weather = {
            'city': "No Info",
            'country_code':'--',
            'temperature': '--',
            'longitude':'--',
            'latitude':'--',
            'feels_like':'--',
            'humidity':'--',
            'pressure':'--',
            'description': '--',
            'icon': '',
        }
        return render(request, 'weather/index.html',city_weather)

