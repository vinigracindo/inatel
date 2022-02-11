from django.test import TestCase


class BaseTestCase(TestCase):
    databases = {'default', 'logs'}
