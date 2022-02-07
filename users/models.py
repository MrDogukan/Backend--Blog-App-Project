from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_pic = models.URLField(blank=True)
    bio = models.TextField(blank=True)