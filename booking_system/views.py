from django.shortcuts import render
from .forms import TableBookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Import messages

# Create your views here.

# Check if the request method is POST (form submitted)
def make_booking(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
# Validate the form and save the data if its valid
        if form.is_valid():
            # Create a new booking instance with out saving it to the database yet
            booking = form.save(commit=False)
            # assign the logged in user to the booking
            booking.user = request.user
            # Save the booking to the database
            booking.save()
            # Add message to say booking successful
            messages.success(request, 'Booking Successful!')

# If its not a POST request display empty form
    else: form = TableBookingForm()
# Load the booking.html template with the form
    return render(request, 'booking.html', {'form': form})