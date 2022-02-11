import datetime

from django.utils import timezone
from django.contrib.auth import get_user_model

from core.tests.base import BaseTestCase as TestCase
from core.models import ScheduleWorkFile


class ScheduleWorkFileModelTest(TestCase):
    def setUp(self):
        self.schedule_file = ScheduleWorkFile.objects.create(
            file='path/to/file.csv',
        )

    def test_create(self):
        self.assertTrue(ScheduleWorkFile.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.schedule_file.created_at, datetime.datetime)
