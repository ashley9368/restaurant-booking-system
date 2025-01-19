from django import forms
from django.contrib.auth.models import User  # Imports built in user model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Extend UserCreationForm to add email field
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Use the built in user model
        # Specify the fields to display to the user
        fields = ['username', 'email', 'password1', 'password2']


# Use django's built in login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
    )
    password = forms.CharField(
        required=True,
    )
