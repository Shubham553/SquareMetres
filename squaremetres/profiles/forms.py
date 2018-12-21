from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UsersForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={}),
        required=True, max_length=35
        )
    # profile_pic =

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_dealer', 'description', 'profile_pic']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UsersForm, self).save(commit=False)
        email = user.email
        try:
            validate_email(email)
        except ValidationError:
            forms.ValidationError('Invalid Email Address')
        user.set_password(self.cleaned_data['password'])
        return user



