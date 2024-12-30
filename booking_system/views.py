from django.shortcuts import render, redirect
from .forms import TableBookingForm
from .models import TableBooking
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages

# Create your views here.

@login_required
# Check if the request method is POST (form submitted)
def make_booking(request):
    # Check if the user already has a booking
    existing_booking = TableBooking.objects.filter(user=request.user).first()

    if existing_booking:
        # Show the existing booking instead of the form
        return render(request, 'booking.html', {'booking': existing_booking})

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
            return redirect('make_booking') # Redirect to booking page to allow user to make a new booking

# If its not a POST request display empty form
    else: form = TableBookingForm()
# Load the booking.html template with the form
    return render(request, 'booking.html', {'form': form})