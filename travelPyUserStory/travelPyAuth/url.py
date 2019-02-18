# customize carRent App URLS Routing from travelPycarRent

from django.conf.urls import url

from travelPyAuth.views import login_view,register_view,home_view

urlpatterns = [
    url(r'^login/', login_view),
	url(r'^signup/', register_view),
    url(r'^home',home_view, name="home"),
]
