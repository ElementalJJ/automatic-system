from django import forms
from django.forms import ModelForm

from .models import Item


class ItemCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        exclude = ["user"]
