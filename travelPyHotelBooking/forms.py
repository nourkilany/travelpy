from django import forms

from .models import HotelReservation

class HotelReservationForm(forms.ModelForm):
    class Meta:
        model = HotelReservation
        fields = ('check_in_date', 'check_out_date', 'number_of_adults')
        CHOICES = ((1, 1), (2, 2),(3, 3),(4, 4),)
        widgets = {
            'check_in_date': forms.DateInput(attrs={'class':'form-control', 'id':'checkin', 'placeholder':'YYYY/MM/DD'}),
            'check_out_date': forms.DateInput(attrs={'class':'form-control', 'id':'checkout', 'placeholder':'YYYY/MM/DD'}),
            'number_of_adults': forms.Select(choices=CHOICES,attrs={'class':'form-control', 'id':'treatment'})
        }
