from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TableBooking, Table
from .forms import TableBookingForm
from django.contrib import messages # Import messages to display feedback to the user

@login_required # Ensure the user is logged in
def manage_booking(request):
    # Get the user's booking from the database
    booking = TableBooking.objects.filter(user=request.user).first()
    editing = False # Checks if the user is editing their booking
    form = None # Start with no form

    if not booking: # If no booking exists, redirect user to the booking page
        return redirect('make_booking')

    # Check if the request is a POST (user clicks button)
    if request.method == "POST":
        if 'delete_booking' in request.POST:
            tables_to_update = list(booking.tables.all())
            for table in booking.tables.all():
                table.status = 'available'
                table.save()

            # Delete the booking
            booking.delete()
            messages.success(request, 'Booking deleted successfully!')
            return redirect('make_booking') # redirect them to make a new booking

        elif 'edit' in request.POST:
            # If the user clicked the Edit booking button, enter edit mode
            editing = True
            form = TableBookingForm(instance=booking) # Show existing booking details

        elif 'save_changes' in request.POST:
            # Save the updated booking
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


    # Render the manage booking page
    return render(request, 'manage_booking.html', {
        'booking': booking, # The users booking details
        'form': form, # The form to edit the booking
        'editing': editing # Weather the user is in edit mode
    })