from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('dojo/create', views.createDojo),
    path('ninja/create', views.createNinja),
    path('dojo/delete', views.delete_dojo)
]