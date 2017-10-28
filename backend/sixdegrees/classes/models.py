from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)