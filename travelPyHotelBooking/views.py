from django.shortcuts import render
from .models import HotelReservation
from .forms import HotelReservationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.


@login_required(login_url='/auth/login')
def index(request):
    if request.method == 'POST':
        form = HotelReservationForm(request.POST)
        print("inside Post")
        if form.is_valid():
            print("isvalid")
            HotelReservation.objects.create(
                check_in_date = request.POST.get("check_in_date"),
                check_out_date = request.POST.get("check_out_date"),
                number_of_adults = request.POST.get("number_of_adults")
            )
            print("form et3mlha submit")
            return HttpResponseRedirect("/hotelBooking")
    form = HotelReservationForm()
    context = {'hotelForm': form}
    return render(request, "travelPyHotelBooking/index.html", context)
