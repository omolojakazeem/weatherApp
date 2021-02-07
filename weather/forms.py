from django import forms
from django.forms import ModelForm
from .models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {'city_name': forms.TextInput(attrs={
            'placeholder': 'Enter City name',
            'class':'input'
        })}
