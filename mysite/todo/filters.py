import django_filters
from django_filters import DateFilter, CharFilter

from todo.models import Item


class ItemFilter(django_filters.FilterSet):
    description = CharFilter(field_name="description", lookup_expr="icontains")

    class Meta:
        model = Item
        fields = "__all__"
        exclude = ["note", "date_created", "date_due", "user"]
