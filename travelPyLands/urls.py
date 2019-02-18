
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'continent/country/city/(?P<cityName>[a-zA-Z]+)$',views.cityPoi, name='cityPoi'),
    url(r'continent/country/city/poi/(?P<poiId>[a-zA-Z0-9.,:-]+)$', views.poiDescription, name='poiDes'),
    url(r'continent/(?P<continentId>[0-9]+)$',views.getcountries,name='countries'),
    url(r'continent/country/(?P<countryId>[a-zA-Z0-9.,:-]+)$',views.getcities, name='cities')
]
