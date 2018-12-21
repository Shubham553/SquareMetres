from django.urls import path
from .views import *

urlpatterns = [
    path('userlogin/', userlogin, name='userlogin'),
    path('register/', register, name='register'),
    path('userlogout/', userlogout, name='userlogout'),
    path('dashboard/<int:user_id>', Dashboard.as_view(), name='dashboard')
]