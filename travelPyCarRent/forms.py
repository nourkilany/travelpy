from django import forms
from .models import CarRental


class CarRentForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = ('pickup_location', 'from_date', 'to_date')
        widgets = {'pickup_location': forms.Select( attrs={'class': 'destination search_input input-location'})}
