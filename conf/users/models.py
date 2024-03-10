from django.contrib.auth.models import AbstractUser
from django.db import models

from api.models import Organization


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    phone_number = models.CharField(
        'Телефон', max_length=11, default=None, blank=True)
    email = models.EmailField(
        'Электронная почта', max_length=150, unique=True, blank=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_organizaton',
        verbose_name='Организация',
    )
