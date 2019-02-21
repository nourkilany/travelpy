
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'city/(?P<cityId>[a-zA-Z0-9.,:-]+)$',views.cityPoi, name='cityPoi'),
    url(r'poi/(?P<cityId>[0-9]+)/(?P<poiId>[a-zA-Z0-9.,:-]+)/(?P<poiName>([a-zA-Z0-9]+\s)*([a-zA-Z0-9]+\s)*[a-zA-Z0-9]+)$', views.poiDescription, name='poiDes'),
    url(r'continent/(?P<continentId>[0-9]+)$',views.getcountries,name='countries'),
    url(r'country/(?P<countryId>[a-zA-Z0-9.,:-]+)$',views.getcities, name='cities')
]
