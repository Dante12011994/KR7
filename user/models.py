from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель "Пользователь"
    Для авторизации пользователя используется email
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
