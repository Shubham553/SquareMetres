from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('userlogin/', userlogin, name='userlogin'),
    path('register/', register, name='register'),
    path('userlogout/', userlogout, name='userlogout'),
    path('dashboard/<int:pk>', login_required(Dashboard.as_view()), name='dashboard'),
    path('user_update/<int:pk>', login_required(UserUpdate.as_view()), name='user_update'),
]