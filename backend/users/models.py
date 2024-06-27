from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
