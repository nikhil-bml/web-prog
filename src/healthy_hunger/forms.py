from django import forms
from .models import Query

class ProductSearchForm(forms.Form):
    name = forms.CharField(max_length=300, required=False, label='Product Name')

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = "__all__"