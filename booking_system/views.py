from django.shortcuts import render, redirect
from .forms import TableBookingForm
from .models import TableBooking, Table
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages

# Create your views here.

# Finds available tables and allocates them based on guest count.


def allocate_tables(guests, date, time):
    # Get all available tables and sort them small to big
    available_tables = (
        Table.objects.filter(status='available')
        .order_by('capacity')
    )
    allocated_tables = []
    # Total number of seats booked so far
    total_capacity = 0

    # Go through available tables and book them until the user has enough seats
    for table in available_tables:
        if total_capacity < guests:  # Check if more seats are still needed
            allocated_tables.append(table)  # Add the table to the booking list
            # Update the total capacity with this table's seats
            total_capacity += table.capacity
        # Check if the required number of seats is reached
        if total_capacity >= guests:
            return allocated_tables  # Return the list of allocated tables

    # If no combination of tables meets the amount needed, return none
    return None


# Booking view
@login_required
# Check if the request method is POST (form submitted)
def make_booking(request):
    # Check if the user already has a booking
    existing_booking = TableBooking.objects.filter(user=request.user).first()

    if existing_booking:
        # Show the existing booking instead of the form
        return render(request, 'booking.html', {'booking': existing_booking})

    # Check if the form was submitted
    if request.method == 'POST':
        # Load the form with the data the user submitted
        form = TableBookingForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Get the number of guests from the form
            guests = int(form.cleaned_data['guests'])
            # Get the date from the form
            date = form.cleaned_data['date']
            # Get the time from the form
            time = form.cleaned_data['time']

            allocated_tables = allocate_tables(guests, date, time)
            if allocated_tables:
                booking = form.save(commit=False)
                # assign the logged in user to the booking
                booking.user = request.user
                # Save the booking to the database
                booking.save()
                booking.tables.set(allocated_tables)

                for table in allocated_tables:
                    table.status = 'booked'
                    table.save()

                # Add message to say booking successful
                messages.success(request, 'Booking Successful!')
                return redirect('make_booking')
            else:
                messages.error(
                    request, 'Sorry there isnt not enough tables available.'
                )

    # If its not a POST request display empty form
    else:
        form = TableBookingForm()
    # Load the booking.html template with the form
    return render(request, 'booking.html', {'form': form})
