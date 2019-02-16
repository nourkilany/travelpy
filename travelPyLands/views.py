from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


api_token = 'XCAO5wKKj26IL5oEdfuwY1TpxjOxnIWTfGW4cik4'


# send data from api to be rendered in index.html

def home(request):

    indexData_dict = {'topCountries': getTopCountriesDataApi(),
                      'topCities': getTopCitiesDataApi()
                      }
    return render(request, "travelPyLands/index.html", context=indexData_dict)


# get one image from api media with any id
def getImageFromApi(id):
    response = requests.get(f'https://api.sygictravelapi.com/1.1/en/places/{id}/media',
                            None, headers={
            'x-api-key': api_token
        })
    imagesData = response.json()
    return imagesData["data"]["media"][0]["url"]


# get top countries from api and return list of them
def getTopCountriesDataApi():
    countriesResponse = requests.get('https://api.sygictravelapi.com/1.1/en/places/list?levels=country&limit=6',
                                     None, headers={
            'x-api-key': api_token
        })
    countriesData = countriesResponse.json()
    countriesList = addImagesToList(countriesData["data"]["places"])
    return countriesList

# get top cities from api and return list of them
def getTopCitiesDataApi():
    citiesResponse = requests.get('https://api.sygictravelapi.com/1.1/en/places/list?levels=city&limit=6',
                                     None, headers={
            'x-api-key': api_token
        })
    citiesData = citiesResponse.json()
    citiesList = addImagesToList(citiesData["data"]["places"])
    return citiesList

# add image  from api to any list of dict with image-> as a key and return list with that image
def addImagesToList(lst):
    for items in lst:
        items["image"] = getImageFromApi(items['id'])
    return lst
