from django import forms
from .models import CarRental
from travelPyLands.views import getApiList

class CarRentForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = ('pickup_location', 'from_date', 'to_date',)
        widgets = {
         'from_date': forms.DateInput(attrs={'type':"date",'class':'check_in search_input', 'id':"datepicker"}),
         'to_date': forms.DateInput(attrs={'type':"date",'class':'check_out search_input', 'id':"datepicker"})}
