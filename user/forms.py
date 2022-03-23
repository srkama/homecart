from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):
    username = forms.CharField(required=True, help_text="username is required and must be unique")
    email = forms.EmailField(required=True, help_text="email is required")

    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')