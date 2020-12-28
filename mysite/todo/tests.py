import datetime

from django.test import TestCase, Client
from django.utils import timezone
from model_bakery import baker

from .models import Item, CustomUser

# Create your tests here.


class ItemTest(TestCase):
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


class HomeTest(TestCase):
    def test_home_view(self):

        c = Client()

        response = c.get("/")

        self.assertEqual(response.status_code, 200)