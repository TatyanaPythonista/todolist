from django.db import models


class User(models.Model):
    """Пользователь"""
    email = models.EmailField(unique=True)
