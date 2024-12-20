from django import forms
from django.contrib.auth.models import User # Imports built in user model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm): # Extend UserCreationForm to add email field
    email = forms.EmailField(required=True) # Add email field and make it required

    class Meta:
        model = User # Use the built in user model
        fields = ['username', 'email', 'password1', 'password2'] # Specify the fields to display to the user

class LoginForm(AuthenticationForm): # Extend django's built in AuthenticationForm for validation
    username = forms.CharField(
        max_length=150,
        required=True,
    )
    password = forms.CharField(
        required=True,
    )