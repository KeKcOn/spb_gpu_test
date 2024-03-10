from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(
        'Электронная почта',
        max_length=150,
        unique=True,
        blank=False,
    )
