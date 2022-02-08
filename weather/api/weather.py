import requests


class OpenWeatherMapAPI:
    """WeatherAPI class for representing and manipulation WeatherOpenMap API
    URL: https://openweathermap.org/api
    """

    URL = 'https://api.openweathermap.org/data/2.5/forecast'

    def __init__(self, api_key):
        self.api_key = api_key

    def __build_url(self, lat, lon):
        """Returns the Open Weather Map API query URL."""
        return '{}?lat={}&lon={}&appid={}&lang=pt_BR&units=metric'.format(OpenWeatherMapAPI.URL, lat, lon, self.api_key)

    def request(self, latitude, longitude):
        """Makes a request to the API."""
        url = self.__build_url(latitude, longitude)
        print(url)
        try:
            response = requests.get(url)
            data = response.json()
            status_code = data['cod']
            if status_code != "200":
                return {'status_code': status_code, 'error': data['message']}
            return data
        except Exception as err:
            return {'status_code': 400, 'error': str(err)}
