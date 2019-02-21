# customize carRent App URLS Routing from travelPycarRent

from django.conf.urls import url

from travelPyAuth.views import login_view,register_view,profile_view,edit_profile,logout

urlpatterns = [
    url(r'^login/', login_view),
	url(r'^signup/', register_view),
    url(r'^profile',profile_view, name="home"),
    url(r'^edit',edit_profile),
    url(r'^logout',logout),

]
