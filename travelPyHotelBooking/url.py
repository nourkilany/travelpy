# customize HotelBooking App URLS Routing from travelPyHotelBooking

from django.conf.urls import url

from travelPyHotelBooking import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
