from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    first_name= None
    last_name = None
    email = models.EmailField(unique=True,blank=False, null=False)
    # REQUIRED_FIELDS = ['email']