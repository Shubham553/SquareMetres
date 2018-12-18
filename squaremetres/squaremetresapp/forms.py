from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email


class BuyerRegisrationForm(forms.Form):
    name = forms.CharField(label='BuyerName', max_length=100)
    address = forms.CharField(label='Your Suggestion', max_length=100, required=False)
    num = forms.IntegerField(label='Mobile No.')


class RealterRegistrationForm(forms.ModelForm):
    class Meta:
        # model = Realter
        fields = '__all__'


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter UserName'}
    ), required=True, max_length=30)

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}
    ), required=True, max_length=30)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'}
    ), required=True, max_length=30)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter LastName'}
    ), required=True, max_length=30)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}
    ), required=True, max_length=30)

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}
    ), required=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            ma = validate_email(email)
        except ValueError:
            raise forms.ValidationError("Invalid Email")
        return email

    def clean_confirm_password(self):
        passd = self.cleaned_data['password']
        confirmpassd = self.cleaned_data['confirm_password']
        if passd != confirmpassd:
            raise forms.ValidationError("Password doesn' match")
        else:
            if len(passd) < 8:
                raise forms.ValidationError("Password must be atleast 18 characters")
            if passd.isdigit():
                raise forms.ValidationError("Password must be alphanumeric characters")


class ChangePasswordForm(forms.ModelForm):

    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old Password",
        required=True)
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password",
        required=True)

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password",
        required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_password']
