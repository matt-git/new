from django import forms

from .models import Login

class LoginForm(forms.ModelForm):
    username = forms.CharField(forms.CharField(label="username", max_length=100),)
    model = Login
        