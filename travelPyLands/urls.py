
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'(?P<countryName>[a-zA-Z]+)/(?P<cityName>[a-zA-Z]+)$',views.cityPoi, name='cityPoi')
]
