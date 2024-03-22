from django import forms
from .models import Manufacturer

class AddCarForm(forms.Form):
    model = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())
    year = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    engine_capacity = forms.DecimalField(max_digits=6, decimal_places=2)
    color = forms.CharField(max_length=50)
