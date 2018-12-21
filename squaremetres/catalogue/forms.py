from .models import Catalogue
from django import forms


class PropertyForm(forms.ModelForm):
    model = Catalogue
    exclude = ('profile', 'date')
