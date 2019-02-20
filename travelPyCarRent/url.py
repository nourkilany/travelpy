# customize carRent App URLS Routing from travelPycarRent

from django.conf.urls import url

from travelPyCarRent import views

urlpatterns = [
    url(r'^$', views.new_car_rent, name='car_rent'),
]
