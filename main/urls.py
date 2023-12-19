# from render import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
