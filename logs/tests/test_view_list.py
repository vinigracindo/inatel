from django.shortcuts import resolve_url as r
from core.tests.base import BaseTestCase as TestCase
from logs.models import Log


class LogListGet(TestCase):
    def setUp(self):
        super(LogListGet, self).setUp()
        self.log = Log(
            endpoint='/',
            user_id='1',
            response_code=200,
            method='POST',
            remote_address='127.0.0.1',
            exec_time=8,
            body_response='response',
            body_request='request'
        )
        self.log.save(using='logs')
        self.response = self.client.get(r('logs:list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'logs/list.html')

    def test_html(self):
        content = [
            (1, '127.0.0.1'),
            (1, 'POST'),
        ]

        for count, expected in content:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        variables = ['logs']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)
