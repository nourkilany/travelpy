from django.shortcuts import render
from django.http import HttpResponse
from .models import CarRental
from .forms import CarRentForm
# Create your views here.


def new_car_rent(request):
    form = CarRentForm()
    if request.method =="POST":
        form = CarRentForm(request.POST)
        if form.is_valid():
            car_request = CarRental.objects.create(
                pickup_location = request.POST.get("pickup_location"),
                from_date  = request.POST.get('from_date'),
                to_date  = request.POST.get('to_date'),
                user_id     = 100,   # user_id ->
                )
    return render(request, 'travelPyCarRent/index.html',{'form':form})
