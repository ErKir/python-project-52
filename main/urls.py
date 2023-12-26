# from render import views
from django.urls import path
from main.views import Index
from users.views import Users

urlpatterns = [
    path('', Index.as_view()),
    path('users', Users.as_view()),
]
