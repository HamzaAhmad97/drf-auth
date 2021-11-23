from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gender_options = [
        ("F", 'female'),
        ("M", 'male'),
        ("C", 'custom')
    ]
    status = [
        ('Single', 'single'),
        ('Married', 'married'),
        ('Widowed', 'widowed')
    ]
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_options, default="M")
    social_status = models.CharField(max_length=10, choices=status, default="Single")

