from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models


class UserProfile(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # first_name = models.CharField(max_length=30, blank=False, null=False)
    # last_name = models.CharField(max_length=30, blank=False, null=False)
    # username = models.CharField(max_length=30, blank=False, null=False)
    age = models.PositiveSmallIntegerField(blank=True, null=True) #validators=[MaxValueValidator(150)]
    gender = models.TextChoices('gender', 'Male Female None')
    photo = models.URLField(null=True)  # TODO: Change to ImageField
    online = models.BooleanField(default=False)
    # email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length=30, blank=True, null=True)  # TODO : need validation
    telegram = models.CharField(max_length=30, blank=True, null=True)  # TODO : need validation
    facebook = models.CharField(max_length=30, blank=True, null=True)  # TODO : need validation
    instagram = models.CharField(max_length=30, blank=True, null=True)  # TODO : need validation
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['created_at', 'first_name']
