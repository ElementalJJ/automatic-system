from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from todo.views import home
from accounts.views import login


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse("home")

        self.assertEqual(resolve(url).func, home)

    def test_login_url_is_resolved(self):
        url = reverse("login")

        self.assertEqual(resolve(url).func, login)