from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from weather.api.weather import OpenWeatherMapAPI
from weather.forms import WeatherForm


def index(request):
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
