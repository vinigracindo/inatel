from django import forms


class WeatherForm(forms.Form):
    lat = forms.CharField(label='Latitude', max_length=32)
    lon = forms.CharField(label='Logintude', max_length=32)
