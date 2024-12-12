from django.db import models
from django.contrib.auth.models import User

# Create your models here. # UNDER CONSTRUCTION :D
class TableBooking(models.Model):
    date = models.DateField() # Date the user wants to book
    user = models.ForignKey(User, on_delete=models.CASCADE) # Links the booking to the user; deletes bookings if the user is removed