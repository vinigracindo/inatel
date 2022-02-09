from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from weather.api.weather import OpenWeatherMapAPI
from weather.forms import WeatherForm


def index(request):
    #url = 'https://api.openweathermap.org/data/2.5/forecast?lat=-9.71369543637303&lon=-36.67114905746711&appid=6d56fbaae0f53bd1fa246a8860c8fb04&lang=pt_BR&units=metric'
    context = {}

    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['lat']
            longitude = form.cleaned_data['lon']
            api = OpenWeatherMapAPI(settings.WEATHER_API_KEY)
            api_data = api.request(latitude, longitude)
            if 'error' in api_data:
                messages.add_message(
                    request, messages.ERROR, api_data['error'])
            else:
                context['api_result_list'] = api_data['list']
                context['api_result_info'] = api_data['city']
    else:
        form = WeatherForm()

    context['form'] = form

    return render(request, 'weather/index.html', context)
