from django.shortcuts import render
from django.http import HttpResponse
from .models import CarRental
from .forms import CarRentForm
from travelPyLands.models import Poi
from travelPyLands.views import getApiList
# Create your views here.






def new_car_rent(request,cityId):
    form = CarRentForm()
    context_dict={'form':form,
                  'pois':getApiList('city', cityId, 'poi', 10)
                  }
    if request.method =="POST":
        form = CarRentForm(request.POST)
        car_request = CarRental.objects.create(
            pickup_location = request.POST.get("pickup_location"),
            from_date  = request.POST.get('from_date'),
            to_date  = request.POST.get('to_date'),
            user_id     = request.session['user_id'],
            )
        print("Form is valid\n")
    return render(request, 'travelPyCarRent/index.html',context=context_dict)
