from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TableBooking
from .forms import TableBookingForm
from django.contrib import messages


# Manages user bookings, Allows editing, deleting.


@login_required  # Ensure user is logged in
def manage_booking(request):
    # Get the user's booking from the database
    booking = TableBooking.objects.filter(user=request.user).first()
    editing = False
    form = None

    if not booking:
        return redirect('make_booking')  # Redirect if no booking exists

    # Check if the request is a POST (user clicks button)
    if request.method == "POST":
        # Free up tables and delete the booking
        if 'delete_booking' in request.POST:
            for table in booking.tables.all():
                table.status = 'available'
                table.save()
            booking.delete()
            messages.success(request, 'Booking deleted successfully!')
            return redirect('make_booking')

        # Edit booking function
        elif 'edit' in request.POST:
            editing = True
            form = TableBookingForm(instance=booking)

        # Save the updated booking
        elif 'save_changes' in request.POST:
            form = TableBookingForm(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                messages.success(request, 'Booking updated successfully!')
                return redirect('manage_booking')

        elif 'cancel_edit' in request.POST:
            # Exit edit mode without saving (if user clicks cancel button)
            return redirect('manage_booking')

    if form is None:
        form = TableBookingForm(instance=booking)

    # Render the manage booking page with booking details.
    return render(request, 'manage_booking.html', {
        'booking': booking,
        'form': form,
        'editing': editing
    })
