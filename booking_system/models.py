from django.db import models
from django.contrib.auth.models import User

# Create your models here. # UNDER CONSTRUCTION :D
class TableBooking(models.Model):
    TIME_SLOTS = [
        ('09:00', '9:00 AM')
    ]
    date = models.DateField() # Date the user wants to book
    time = models.TimeField() # Time the user would like to book
    guests = models.PositiveIntegerField(default=1) # Sets the default number of guests to 1
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Links the booking to the user; deletes bookings if the user is removed