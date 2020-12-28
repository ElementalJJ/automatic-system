from django.shortcuts import render
from django.http import HttpResponse

from .models import Item, CustomUser

# Create your views here.


def home(request):

    try:
        items = request.user.item_set.all().order_by("-date_due")
    except AttributeError:
        items = None

    context = {"items": items}

    return render(request, "todo/index.html", context)