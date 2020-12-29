import datetime

from django.test import Client, TestCase
from django.utils import timezone
from model_bakery import baker

from accounts.models import CustomUser
from todo.models import Item

# Create your tests here.


class TestModels(TestCase):
    def test_item_due_soon_true(self):
        item = baker.make_recipe("todo.item_due_soon")

        self.assertTrue(isinstance(item, Item))
        self.assertTrue(item.due_soon())

    def test_item_due_soon_false(self):
        item = baker.make_recipe("todo.item_not_due_soon")

        self.assertTrue(isinstance(item, Item))
        self.assertFalse(item.due_soon())

    def test_item_name(self):
        item = baker.make(Item)

        self.assertTrue(isinstance(item, Item))
        self.assertEqual(item.__str__(), item.name)

    def test_user_name(self):
        user = baker.make(CustomUser)

        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.__str__(), user.username)
