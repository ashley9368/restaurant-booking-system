from django.shortcuts import render

# Create your views here.
def make_booking(request):
    return render(request, 'booking.html') # Path to booking.html in templates folder