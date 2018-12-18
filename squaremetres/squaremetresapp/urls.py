from django.conf.urls import url
from .views import *

urlpatterns = [
    url('', index),
    url('about/', about),
    url('contact/', index),
    url('properties/', index),
]
