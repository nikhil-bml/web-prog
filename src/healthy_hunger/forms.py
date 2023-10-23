from django import forms
from .models import Product

class ProductSearchForm(forms.Form):
    name = forms.CharField(max_length=300, required=False, label='Product Name')
