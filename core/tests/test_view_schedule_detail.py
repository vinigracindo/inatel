from django.shortcuts import resolve_url as r
from django.utils import timezone
from core.tests.base import BaseTestCase as TestCase
from core.models import ScheduleWork, ScheduleWorkFile


class ScheduleDetailGet(TestCase):
    def setUp(self):
        super(ScheduleDetailGet, self).setUp()
        self.schedule_file = ScheduleWorkFile.objects.create(
            file='path/to/file.csv',
        )
        self.schedule = ScheduleWork.objects.create(
            file=self.schedule_file,
            technician_name='foo',
            technician_register='00001',
            description='lorem impsum',
            date=timezone.now()
        )
        self.response = self.client.get(
            r('core:schedule-detail', self.schedule.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/schedule-detail.html')

    def test_context(self):
        variables = ['schedule', 'schedules']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)
