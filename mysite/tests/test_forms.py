import datetime

from django.test import TestCase, SimpleTestCase
from model_bakery import baker
from django.utils import timezone

from todo.models import Item
from todo.forms import ItemCreationForm
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class TestForms(SimpleTestCase):
    def test_item_creation_form_valid_data(self):
        form = ItemCreationForm(
            data={
                "name": "Test",
                "description": "This might be a test.",
                "note": "This is a test.",
                "date_created": timezone.now(),
                "date_due": timezone.now() + datetime.timedelta(days=2),
                "user": None,
            }
        )

        self.assertTrue(isinstance(form, ItemCreationForm))
        self.assertTrue(form.is_valid())

    def test_item_creation_form_no_data(self):
        form = ItemCreationForm(data={})

        self.assertTrue(isinstance(form, ItemCreationForm))
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
