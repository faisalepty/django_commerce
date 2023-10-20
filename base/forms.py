from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'User Name', 'class':'username'}),
            'email': forms.TextInput(attrs={'placeholder':'email', 'class':'username'}),

            'password1': forms.PasswordInput(attrs={'placeholder':'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),
        }


    
class QuantityForm(ModelForm):
    class Meta:
        model = Oder
        fields = ['quantity']
        widgets = {
            'quantity':forms.NumberInput(attrs={'class':'form-control input-number text-center', 'min':1, 'max':100})
        }