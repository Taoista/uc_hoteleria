from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hoteles/create', views.create, name="index"),
    path('hoteles/ver', views.ver, name="ver"),
]