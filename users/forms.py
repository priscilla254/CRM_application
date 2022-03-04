# from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields='__all__'
        exclude=['user']