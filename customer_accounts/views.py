from .forms import SignupForm
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages  # To display messages to the user

""" Handles user signup by displaying a
form and saving the users details on submission
"""


def signup(request):
    # If user tries to access signup, take them home
    if request.user.is_authenticated:
        return redirect('homepage')

    # Check if the form is submitted
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # Validate the form and save the data if its valid
        if form.is_valid():
            form.save()
            # redirects user to login page
            return redirect('login')
    else:
        form = SignupForm()  # Show empty signup form
    # Render the SignUp page
    return render(request, 'signup.html', {'form': form})

# validates the user credentials and logs them in


def login_view(request):
    # If user tries to access login, take them home
    if request.user.is_authenticated:
        return redirect('homepage')

    # Use submitted data if available, otherwise show empty form
    form = LoginForm(data=request.POST or None)
    # Check if the form is submitted
    if request.method == 'POST':
        # Validate the form data
        if form.is_valid():
            # Get username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            # If authentication is succesful, log the user in
            if user is not None:
                login(request, user)
                return redirect('homepage')  # redirect to homepage after Login

            else:  # Message to tell user they entered their details wrong
                messages.error(request, 'Invalid username or password.')
    # Render the login page with the form
    return render(request, 'login.html', {'form': form})
