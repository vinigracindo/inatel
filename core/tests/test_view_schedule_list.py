from django.shortcuts import resolve_url as r
from core.tests.base import BaseTestCase as TestCase
from core.models import ScheduleWorkFile


class ScheduleListGet(TestCase):
    def setUp(self):
        super(ScheduleListGet, self).setUp()
        self.schedule_file = ScheduleWorkFile.objects.create(
            file='path/to/file.csv',
        )
        self.response = self.client.get(r('core:schedule-list'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/schedule-list.html')

    def test_html(self):
        content = [
            ('path/to/file.csv'),
        ]

        for expected in content:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        variables = ['schedules']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)
