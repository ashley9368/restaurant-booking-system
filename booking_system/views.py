from django.shortcuts import render
from .forms import TableBookingForm

# Create your views here.

# Check if the request method is POST (form submitted)
def make_booking(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
# Validate the form and save the data if its valid
        if form.is_valid():
            form.save()
# If its not a POST request display empty form
    else: form = TableBookingForm()
# Load the booking.html template with the form
    return render(request, 'booking.html', {'form': form})