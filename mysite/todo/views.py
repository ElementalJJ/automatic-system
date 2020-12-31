from django.shortcuts import render
from django.http import HttpResponse

from .models import Item, CustomUser
from .filters import ItemFilter

# Create your views here.


def home(request):

    try:
        items = request.user.item_set.all().order_by("-date_due")
    except AttributeError:
        items = None

    myFilter = ItemFilter(request.GET, queryset=items)

    context = {"items": items, "myFilter": myFilter}

    return render(request, "todo/index.html", context)