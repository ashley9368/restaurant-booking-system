from django.shortcuts import render
from .models import TableBooking

# Create your views here.
def make_booking(request):
    return render(request, 'booking.html') # Path to booking.html in templates folder

def user_bookings(request):
    bookings = TableBooking.objects.filter(user=request.user) # Gets table booking data
    return render(request, 'booking.html', {bookings})