from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse('Hello Index!')
    return render(request, "travelPyLands/index.html")

# https://api.sygictravelapi.com/1.1/en/places/list?levels=city&limit=6 -> cities limit 6

# https://api.sygictravelapi.com/1.1/en/places/list?levels=country&limit=6 -> country limit 6
