from django import forms  # pragma: no cover
from django.forms import ModelForm  # pragma: no cover

from .models import Item  # pragma: no cover


class CreateItemForm(ModelForm):  # pragma: no cover
    class Meta:
        model = Item
        fields = "__all__"
        exclude = ["user"]