from django.db import models
from datetime import datetime
# Create your models here.


class Enquiry(models.Model):
    property_name = models.CharField(max_length=200)
    property_id = models.IntegerField()
    user = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    enquiry_date = models.DateTimeField(default=datetime.now, blank=True)
    buyer_id = models.IntegerField(blank=True)
    dealer_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
