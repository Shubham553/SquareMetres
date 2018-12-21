from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    is_dealer = models.BooleanField('Dealer', default=False)
    description = models.TextField(blank=True)
    registration_date = models.DateTimeField(default=date.today, blank=True)
    profile_pic = models.ImageField(upload_to='user/', null=True, blank=True, default='/static/images/default_pic.png')

