from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    # path('property/<int:property_id>/', PropertyView.as_view(), name='property'),
    path('about_us/', TemplateView.as_view(template_name='about.html'), name='about_us'),
    path('properties_list/', properties, name='properties'),
    path('contact_us/', TemplateView.as_view(template_name='contact.html'), name='contact_us'),
    path('property/<int:id>/', property, name='property'),
    path('properties/', properties, name='properties'),
    path('add_property/', login_required(AddProperty.as_view()), name='add_property'),
    path('search/', SearchView.as_view(), name='search'),
]