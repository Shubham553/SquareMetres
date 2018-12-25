from django.db.models import Q
from datetime import date
from profiles.models import UserProfile
from django.db import models
# Create your models here.


class SearchProperties(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) |
                         Q(city__icontains=query) |
                         Q(state__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs


class Catalogue(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    area = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                   default='/static/images/defaults/default_property.jpeg')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                default='/static/images/defaults/default_property.jpeg')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                default='/static/images/defaults/default_property.jpeg')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                default='/static/images/defaults/default_property.jpeg')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                default='/static/images/defaults/default_property.jpeg')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                default='/static/images/defaults/default_property.jpeg')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                default='/static/images/defaults/default_property.jpeg')
    is_published = models.BooleanField(default=True)
    catalogue_date = models.DateTimeField(default=date.today, blank=True)
    objects = SearchProperties()

    def __str__(self):
        return self.title


