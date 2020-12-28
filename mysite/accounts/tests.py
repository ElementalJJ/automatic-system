from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from .models import CustomUser

# Create your tests here.


class UserTest(TestCase):
    def test_user_name(self):
        user = baker.make(CustomUser)
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.__str__(), user.username)