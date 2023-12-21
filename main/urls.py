# from render import views
from django.urls import path
from main.views import Index

urlpatterns = [
    path('', Index.as_view()),
]
