from django.shortcuts import render

import requests

from django.http import HttpResponse

from travelPyUserBlog.models import Cities

import json

# Create your views here.


def index(request):

    api_token = 'XCAO5wKKj26IL5oEdfuwY1TpxjOxnIWTfGW4cik4'
    response = requests.get('https://api.sygictravelapi.com/1.1/en/places/list?levels=city',
                            None, headers={
            'x-api-key': api_token
        })
    citiesData = response.json()
    citiesData_dict = {'citiesPlaces':citiesData["data"]["places"]}
    return render(request, 'travelPyUserBlog/index.html', context=citiesData_dict)


def cities(request, country_name):

    cities_list = Cities.objects.filter(cityCountry=country_name).order_by('cityName').iterator()
    cities_dict = {'cities': cities_list}
    ay7aga()
    return render(request, 'travelPyUserBlog/cities.html', context=cities_dict)



def ay7aga():

    print("ay7aga5ara")