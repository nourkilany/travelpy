# customize carRent App URLS Routing from travelPycarRent

from django.conf.urls import url

from travelPyCarRent import views

urlpatterns = [
    url(r'(?P<cityId>[a-zA-Z0-9.,:-]+)$', views.new_car_rent, name='car_rent'),
]
