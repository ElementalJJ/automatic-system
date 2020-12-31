from django.urls import path
from . import views

urlpatterns = [
    path("api/items/", views.apiOverview, name="api-overview"),
    path("api/item-list/", views.itemList, name="item-list"),
    path("api/item-detail/<str:pk>/", views.itemDetail, name="item-detail"),
    path("api/item-create/", views.itemCreate, name="item-create"),
    path("api/item-update/<str:pk>/", views.itemUpdate, name="item-update"),
    path("api/item-delete/<str:pk>/", views.itemDelete, name="item-delete"),
]