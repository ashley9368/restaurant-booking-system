from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TableBooking(models.Model):
    date = models.DateField() # Date the user wants to book