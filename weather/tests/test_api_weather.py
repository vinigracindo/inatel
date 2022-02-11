from unittest.mock import patch

from core.tests.base import BaseTestCase as TestCase
from weather.api.weather import OpenWeatherMapAPI


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({'cod': '200', 'data': 'success'}, 200)


def mocked_requests_invalid_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({'cod': '400', 'data': 'insuccess'}, 400)


class OpenWeatherMapAPITest(TestCase):
    def setUp(self):
        self.api_key = 'api_key'
        self.api = OpenWeatherMapAPI(self.api_key)

    def test_has_url_as_constant(self):
        self.assertTrue(hasattr(self.api, 'URL'))

    def test_build_url(self):
        url = self.api._OpenWeatherMapAPI__build_url('-1.111', '-2.222')
        expected_url = '{}?lat=-1.111&lon=-2.222&appid={}&lang=pt_BR&units=metric'.format(
            self.api.URL, self.api_key)
        self.assertEqual(url, expected_url)

    @patch('weather.api.weather.requests.get', mocked_requests_get)
    def test_valid_request(self):
        response = self.api.request('lat', 'lon')
        self.assertTrue('data' in response.keys())

    @patch('weather.api.weather.requests.get', mocked_requests_invalid_get)
    def test_invalid_request(self):
        response = self.api.request('lat', 'lon')
        self.assertTrue('error' in response.keys())
        self.assertTrue('status_code' in response.keys())
