from django.shortcuts import render

from django.http import HttpResponse

from travelPyUserBlog.models import Cities

# Create your views here.


def index(request):

    return render(request, 'travelPyUserBlog/index.html')


def cities(request):

    cities_list = Cities.objects.filter(cityCountry='DE')
    cities_dict = {'cities': cities_list}
    return render(request, 'travelPyUserBlog/cities.html', context=cities_dict)
