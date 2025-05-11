from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser) : 
    last_name = None
    first_name = None

    def __str__(self):
        return self.username
