from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name="Correo Electronico", unique=True)

    def __str__(self):
        return self.username
