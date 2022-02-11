import datetime

from django.utils import timezone

from core.tests.base import BaseTestCase as TestCase
from core.models import ScheduleWork, ScheduleWorkFile


class ScheduleWorkModelTest(TestCase):
    def setUp(self):
        file = ScheduleWorkFile.objects.create(
            file='path/to/file.csv',
        )

        self.schedule = ScheduleWork.objects.create(
            file=file,
            technician_name='foo',
            technician_register='00001',
            description='lorem impsum',
            date=timezone.now()
        )

    def test_create(self):
        self.assertTrue(ScheduleWork.objects.exists())

    def test_str(self):
        self.assertEqual('{}'.format(self.schedule.pk), str(self.schedule))

    def test_created_at(self):
        self.assertIsInstance(self.schedule.created_at, datetime.datetime)
