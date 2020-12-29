from django.test import Client, TestCase
from django.urls import reverse


class TestViewsTodo(TestCase):
    def test_home_view_GET(self):
        c = Client()

        response = c.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/index.html")


class TestViewsAccounts(TestCase):
    def test_login_view_GET(self):
        c = Client()

        response = c.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/main.html")
