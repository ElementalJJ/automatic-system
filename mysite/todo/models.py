import datetime

from django.db import models
from django.utils import timezone

from accounts.models import CustomUser

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_due = models.DateField("Due date", null=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)

    def due_soon(self):
        now = timezone.now()
        return self.date_due <= now + datetime.timedelta(days=5)

    def __str__(self):
        return self.name