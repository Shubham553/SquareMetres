from .models import Catalogue
from django import forms


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        exclude = ('catalogue_date',)
