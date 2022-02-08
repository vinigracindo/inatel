from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url as r


class LoginGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('login'))

    def test_get(self):
        """GET /login/ must return status code 200."""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use core/login.html as template."""
        self.assertTemplateUsed(self.response, 'login.html')

    def test_csrf(self):
        """HTML must contains CSRF in form."""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_html(self):
        """HTML must contains username, password and CSRF fields.
        Must contains submit button and form method post
        """
        tags = (
            ('<form', 1),
            ('<input', 3),
            ('name="username"', 1),
            ('name="password"', 1),
            ('type="submit"', 1),
            ('method="post"', 1),
        )

        for tag, count in tags:
            with self.subTest():
                self.assertContains(self.response, tag, count)

    def test_form_has_fields(self):
        """form must have 2 fields (username and password)"""
        form = self.response.context['form']
        self.assertSequenceEqual(['username', 'password'], list(form.fields))


class LoginPost(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user('user', 'user@mail.com', 'pass')
        data = dict(username=user.username, password='pass')
        self.response = self.client.post(r('login'), data)

    def test_post(self):
        """POST /login/ must return 302 status code (redirect after success login)"""
        self.assertEqual(302, self.response.status_code)

    def test_user_is_auth(self):
        """Must have a session after success login"""
        session = self.response.wsgi_request.session
        self.assertIn('_auth_user_id', session)


class LoginInvalidPost(TestCase):
    def setUp(self):
        data = dict(username='user_does_not_exist', password='pass')
        self.response = self.client.post(r('login'), data)

    def test_invalid_user_post(self):
        """Invalid Post should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_html(self):
        """HTML must contains error messages."""
        form = self.response.context['form']
        errors = form.non_field_errors()

        for error in errors:
            with self.subTest():
                self.assertContains(self.response, error)
