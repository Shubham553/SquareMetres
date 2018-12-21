from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about_us/', about, name='about_us'),
    path('properties_list/', properties, name='properties'),
    path('contact_us/', contactus, name='contact_us'),
    path('property<int:property_id>', property, name='property'),
    path('properties/', properties, name='properties'),
    path('add_property/', AddProperty.as_view(), name='postproperty'),
    # path('search', search, name='search'),
]