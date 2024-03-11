from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import MAX_LENGTH_PHONE_NUMBER, MAX_LENGTH_EMAIL
from .validators import validate_phone_number
from api.models import Organization


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    phone_number = models.CharField(
        'Телефон',
        max_length=MAX_LENGTH_PHONE_NUMBER,
        validators=(validate_phone_number,),
        default=None,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=MAX_LENGTH_EMAIL,
        unique=True,
        blank=False,
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_organizaton',
        verbose_name='Организация',
    )
