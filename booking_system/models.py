from django.db import models
from django.contrib.auth.models import User

# Monday - Sunday: 9:00 AM - 9:00 PM

# Create your models here.

# Times avaliable for booking
TIME_SLOTS = [
    ('12:00', '12:00 PM'),
    ('13:00', '13:00 PM'),
    ('14:00', '14:00 PM'),
    ('15:00', '15:00 PM'),
    ('16:00', '16:00 PM'),
    ('17:00', '17:00 PM'),
    ('18:00', '18:00 PM'),
    ('19:00', '19:00 PM'),
    ('20:00', '20:00 PM'),
]

# This model represents a table in a restaurant


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=[('available', 'Available'), ('booked', 'Booked')],
        default='available'
    )

    """
    Provides better readability for
    the admin interface instead of a random reference
    """
    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"


"""
Stores table bookings with date, time, guests, and customer details.
Each booking is linked to a user and can include multiple tables.
If a user is deleted, their bookings are removed
"""


class TableBooking(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_SLOTS)
    guests = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    tables = models.ManyToManyField(Table)

    """
    Provides better readability for the admin interface
    instead of a random reference
    """
    def __str__(self):
        return (
            f"Booking by {self.first_name} {self.last_name} "
            f"for {self.guests} guests"
        )
