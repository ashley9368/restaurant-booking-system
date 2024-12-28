from django.db import models
from django.contrib.auth.models import User

# Monday - Sunday: 9:00 AM - 9:00 PM

# Create your models here. # UNDER CONSTRUCTION :D

#Times avaliable for booking
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

class TableBooking(models.Model):
    date = models.DateField() # Date the user wants to book
    time = models.CharField(max_length=5, choices=TIME_SLOTS) # Time the user would like to book
    guests = models.PositiveIntegerField(default=1) # Sets the default number of guests to 1
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Links the booking to the user; deletes bookings if the user is removed
    first_name = models.CharField(max_length=100, default="") # First name for the booking
    last_name = models.CharField(max_length=100, default="") # Last name for the booking
    email = models.EmailField(max_length=100, default="") # Email for customer