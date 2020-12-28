import datetime
from django.utils import timezone

from model_bakery.recipe import Recipe
from todo.models import Item

recent_time = timezone.now() + datetime.timedelta(days=4, hours=23, seconds=59)

longer_time = timezone.now() + datetime.timedelta(days=5, seconds=1)


item_due_soon = Recipe(Item, date_due=recent_time)

item_not_due_soon = Recipe(Item, date_due=longer_time)