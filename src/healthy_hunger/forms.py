from django import forms
from .models import Query
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductSearchForm(forms.Form):
    name = forms.CharField(max_length=300, required=False, label="Product Name")


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = "__all__"


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
