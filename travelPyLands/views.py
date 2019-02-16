from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


# https://api.sygictravelapi.com/1.1/en/places/list?levels=city&limit=6 -> cities limit 6

# https://api.sygictravelapi.com/1.1/en/places/list?levels=country&limit=6 -> country limit 6

api_token = 'XCAO5wKKj26IL5oEdfuwY1TpxjOxnIWTfGW4cik4'

def home(request):
    # return HttpResponse('Hello Index!')
    # api_token = 'XCAO5wKKj26IL5oEdfuwY1TpxjOxnIWTfGW4cik4'

    countriesData_dict = {'topCountries': getCountriesDataApi()}
    return render(request, "travelPyLands/index.html", context=countriesData_dict)

def getImageFromApi(id):
    response = requests.get(f'https://api.sygictravelapi.com/1.1/en/places/{id}/media',
                            None, headers={
            'x-api-key': api_token
        })
    imagesData = response.json()
    return imagesData["data"]["media"][0]["url"]

def getCountriesDataApi():
    countriesResponse = requests.get('https://api.sygictravelapi.com/1.1/en/places/list?levels=country',
                                     None, headers={
            'x-api-key': api_token
        })
    countriesData = countriesResponse.json()
    countriesList = addImagesToList(countriesData["data"]["places"])
    return countriesList

def addImagesToList(lst):
    for items in lst:
        items["image"] = getImageFromApi(items['id'])
    return lst
