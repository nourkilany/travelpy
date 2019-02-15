from django.conf.urls import url, include
from django.contrib import admin

# to keep urls project clean use
# url(r'^blog/', include('travelPyUserBlog.url'))
# then create url.py with your app routing -> check -> travelPyUserBlog/url.py

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # pylands urls
    url(r'^', include("travelPyLands.urls")),
    # pyblogs urls
    url(r'^blog/', include('travelPyUserBlog.url')),
    # pyhotels urls
    url(r'^hotelBooking/', include('travelPyHotelBooking.url')),
    # pycarrent urls
    url(r'^carRental/', include('travelPyCarRent.url'))
]
