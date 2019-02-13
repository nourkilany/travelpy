# customize HotelBooking App URLS Routing from travelPyHotelBooking

from django.conf.urls import url

from travelPyCarRent import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
