from django.shortcuts import render
from .models import HotelReservation
from travelPyLands.models import City,Hotel
from .forms import HotelReservationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='/user/login')
def index(request,cityId,poiId):

    if request.method == 'POST':
        form = HotelReservationForm(request.POST)
        print("inside Post")
        if form.is_valid():
            print("isvalid")
            print(Hotel.objects.filter(id = int(poiId[4:])))
            HotelReservation.objects.create(
                check_in_date = request.POST.get("check_in_date"),
                check_out_date = request.POST.get("check_out_date"),
                number_of_adults = request.POST.get("number_of_adults"),
                user_id = request.user.id,
                city = City.objects.filter(id = cityId).first()
            )
            print("form et3mlha submit")
            return HttpResponseRedirect("/hotelBooking")
    form = HotelReservationForm()
    context = {'hotelForm': form}
    return render(request, "travelPyHotelBooking/index.html", context)
