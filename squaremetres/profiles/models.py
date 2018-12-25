from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    is_dealer = models.BooleanField('Dealer', default=False)
    description = models.TextField(blank=True)
    registration_date = models.DateTimeField(default=datetime.now, blank=True)
    profile_pic = models.ImageField(upload_to='user_pic/', null=True, blank=True,
                                    default='/static/images/defaults/default_pic.png')

