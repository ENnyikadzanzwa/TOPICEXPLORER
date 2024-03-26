from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import  User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email','education_level', 'password1', 'password2']
