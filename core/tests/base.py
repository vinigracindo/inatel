from django.test import TestCase
from django.contrib.auth import get_user_model


class BaseTestCase(TestCase):
    databases = {'default', 'logs'}

    def setUp(self):
        self.user_logged_in = get_user_model().objects.create_user(
            username='username', password='password')
        self.response = self.client.login(
            username='username', password='password')
