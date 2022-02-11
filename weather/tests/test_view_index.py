from unittest.mock import MagicMock, patch

from core.tests.base import BaseTestCase as TestCase

from django.conf import settings
from django.shortcuts import resolve_url as r
from django.contrib.messages import get_messages

from weather.api.weather import OpenWeatherMapAPI


class IndexGet(TestCase):
    def setUp(self):
        super(IndexGet, self).setUp()
        self.response = self.client.get(r('weather:index'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'weather/index.html')

    def test_html(self):
        contents = [
            (1, '<form'),
            (3, '<input'),
            (1, 'type="submit"'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        variables = ['form']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)


mock_class = OpenWeatherMapAPI(settings.WEATHER_API_KEY)

fake_data_list = {'dt': 1644537600,
                  'main': {'temp': 24.98, 'feels_like': 25.31, 'temp_min': 24.98,
                           'temp_max': 24.98, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 978,
                           'humidity': 68, 'temp_kf': 0},
                  'weather': [{'id': 803, 'main': 'Clouds', 'description': 'nublado', 'icon': '04n'}],
                  'clouds': {'all': 72},
                  'wind': {'speed': 6.16, 'deg': 83, 'gust': 10.77}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'},
                  'dt_txt': '2022-02-11 00:00:00'}

fake_data_city = {'id': 3979802, 'name': 'Zamora',
                  'coord': {'lat': 19.9853, 'lon': -102.2819},
                  'country': 'MX', 'population': 15000, 'timezone': -21600, 'sunrise': 1644499260, 'sunset': 1644540352}

mock_class.request = MagicMock(
    return_value={'cod': '200', 'message': 0, 'list': fake_data_list, 'city': fake_data_city})


class IndexPost(TestCase):
    @patch("weather.api.weather.OpenWeatherMapAPI.request", mock_class.request)
    def setUp(self):
        super(IndexPost, self).setUp()
        data = dict(
            lat='1234',
            lon='1234'
        )
        self.response = self.client.post(r('weather:index'), data)

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use weather/index.html."""
        self.assertTemplateUsed(self.response, 'weather/index.html')


mock_class.request = MagicMock(
    return_value={'cod': '400', 'error': 'wrong data'})


class IndexInvalidPost(TestCase):
    @patch("weather.api.weather.OpenWeatherMapAPI.request", mock_class.request)
    def setUp(self):
        super(IndexInvalidPost, self).setUp()
        data = dict(
            lat='wrong_value',
            lon='wrong_value'
        )
        self.response = self.client.post(r('weather:index'), data)

    def test_has_message_error(self):
        messages = list(get_messages(self.response.wsgi_request))
        self.assertTrue(messages)
