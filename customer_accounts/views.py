from django.shortcuts import render
from .forms import SignupForm
from django.shortcuts import redirect
from .forms import LoginForm

# Create your views here.

# Check if the request method is POST (form submitted)
def signup(request): 
    if request.method == 'POST':
        form = SignupForm(request.POST)
# Validate the form and save the data if its valid
        if form.is_valid(): 
            form.save()
            # redirects user to login page
            return redirect('login')
    else: 
        form = SignupForm()
# Load the signup.html template with the form
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm(data=request.POST or None) # Use submitted data if available, otherwise show empty form
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username') # Get the username from the form after checking the input
            password = form.cleaned_data.get('password')