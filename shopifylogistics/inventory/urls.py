from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('add_warehouse/', views.add_warehouse, name='add_warehouse'),
    path('edit_inventory/<slug:id>', views.edit_inventory, name='edit_inventory'),
    path('delete_inventory/<slug:id>', views.delete_inventory, name='delete_inventory'),
]