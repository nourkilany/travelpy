
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'(?P<countryName>([a-zA-Z0-9]+\s)*[a-zA-Z0-9]+)/(?P<cityName>[a-zA-Z]+)$',views.cityPoi, name='cityPoi'),
    url(r'(?P<poiId>[a-zA-Z0-9.,:-]+)$',views.poiDescription,name='poiDes'),
]
