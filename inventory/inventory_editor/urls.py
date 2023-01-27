from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('img.jpg', views.img, name="index"),
    path('items', views.get_items, name="get_items"),
    path('items/new', views.add_item, name="add_item"),
    path('items/search', views.get_items_search, name="get_items_search"),
    path('items/update', views.update_item, name='update_item')

]

