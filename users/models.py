from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    fullname = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
