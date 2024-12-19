from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['date', 'time', 'guests', 'first_name', 'last_name', 'email']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=TableBooking._meta.get_field('time').choices),
        }
