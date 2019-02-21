# customize HotelBooking App URLS Routing from travelPyHotelBooking

from django.conf.urls import url

from travelPyHotelBooking import views

urlpatterns = [
    url(r'(?P<cityId>[0-9]+)/(?P<poiName>([a-zA-Z0-9]+\s)*([a-zA-Z0-9]+\s)*[a-zA-Z0-9]+)$', views.index, name='index'),
]
