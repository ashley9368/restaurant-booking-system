from django.shortcuts import render
from .forms import SignupForm

# Create your views here.

# Check if the request method is POST (form submitted)
def signup(request): 
    if request.method == 'POST':
        form = SignupFrom(request.POST)