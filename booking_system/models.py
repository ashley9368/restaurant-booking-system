from django.db import models
from django.contrib.auth.models import User

# Monday - Sunday: 9:00 AM - 9:00 PM

# Create your models here. # UNDER CONSTRUCTION :D                                 
class TableBooking(models.Model):
    TIME_SLOTS = [
        ('09:00', '9:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
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
    date = models.DateField() # Date the user wants to book
    time = models.CharField(max_length=5, choices=TIME_SLOTS) # Time the user would like to book
    guests = models.PositiveIntegerField(default=1) # Sets the default number of guests to 1
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Links the booking to the user; deletes bookings if the user is removed
