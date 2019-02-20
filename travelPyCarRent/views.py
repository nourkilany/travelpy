from django.shortcuts import render
from django.http import HttpResponse
from .models import CarRental
from .forms import CarRentForm
from travelPyLands.models import Poi
# Create your views here.


def new_car_rent(request):
    form = CarRentForm()
    form.fields["pickup_location"].queryset = Poi.objects.filter(city_id = 101)
    if request.method =="POST":
        form = CarRentForm(request.POST)
        car_request = CarRental.objects.create(
            pickup_location_id = request.POST.get("pickup_location"),
            from_date  = request.POST.get('from_date'),
            to_date  = request.POST.get('to_date'),
            user_id     = request.session['user_id'],
            )
        print("Form is valid\n")
    return render(request, 'travelPyCarRent/index.html',{'form':form})
