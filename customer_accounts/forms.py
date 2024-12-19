from django import forms
from django.contrib.auth.models import User # Imports built in user model
from django.contrib.auth.forms import UserCreationFrom

class SignupForm(UserCreationForm): # Extend UserCreationForm to add email field
    email = forms.EmailField(required=True) # Add email field and make it required

    class Meta:
        model = User # Use the built in user model
        fields = ['Username', 'email', 'password1', 'password2'] # Specify the fields to display to the user