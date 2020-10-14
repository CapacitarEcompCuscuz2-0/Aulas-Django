from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    GROUPS_CHOICES = [('adm', 'ADM'), ('eng', 'ENG'), ('tec', 'TEC')]

    first_name = models.CharField(editable=False, max_length=1)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=16)
    group = models.CharField(max_length=6, choices=GROUPS_CHOICES)
    photo = models.ImageField(verbose_name="foto", upload_to="fotos/", default="default.jpg")