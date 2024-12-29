from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TableBooking


@login_required
def manage_booking(request):
    # Get the logged-in user's booking
    booking = TableBooking.objects.filter(user=request.user).first()

    if not booking:
        #If no booking exists, redirect to the booking page
        return redirect('make_booking')

    # Render the manage booking page
    return render(request, 'manage_booking.html', {'booking': booking})