from django.contrib.auth import get_user_model

from core.tests.base import BaseTestCase as TestCase

from logs.models import Log


class LogModelTest(TestCase):
    def setUp(self):
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

    def test_create(self):
        self.assertTrue(Log.objects.exists())

    def test_get_user(self):
        get_user_model().objects.create_user('foo', 'foo@bar.com', 'foopass')
        self.assertEqual(str(self.log.get_user_object()), 'foo')

    def test_get_user_anonymous(self):
        self.assertEqual(self.log.get_user_object(), 'Usuário anônimo')
