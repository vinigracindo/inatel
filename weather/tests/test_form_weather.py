from core.tests.base import BaseTestCase as TestCase
from weather.forms import WeatherForm


class WeatherFormTest(TestCase):

    def setUp(self):
        self.form = WeatherForm()

    def test_form_has_fields(self):
        """WeatherForm must have lat (latitude) and lon (longitude) fields."""
        expected = ['lat', 'lon']
        self.assertEqual(expected, list(self.form.fields))
