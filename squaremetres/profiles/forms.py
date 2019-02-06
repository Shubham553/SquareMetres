from django import forms
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
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'is_dealer', 'description', 'profile_pic']

        def save(self, commit=True):
            user = super(UserUpdateForm, self).save(commit=False)
            if commit:
                user.save()
            return user




