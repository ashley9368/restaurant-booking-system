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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Change the 'guests' field to a dropdown
        self.fields['guests'] = forms.ChoiceField(
            choices= [ 
                (1, '1'),
                (2, '2'),
                (3, '3'),
                (4, '4'),
                (5, '5'),
                (6, '6'),
                (7, '7'),
                (8, '8'),
            ], 
            label="Guests" #
        )
