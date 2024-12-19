from django.shortcuts import render
from .forms import TableBookingForm

# Create your views here.
def make_booking(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)

        if form.is_valid():
            form.save()

        else: form = TableBookingForm()

    return render(request, 'booking.html', {'form': form})