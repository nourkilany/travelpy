# customize UserBlog App URLS Routing from travelPyUserBlog

from django.conf.urls import url

from travelPyUserStory import views

urlpatterns = [
    url(r'^$', views.all),
    url(r'^new/$', views.new),
    url(r'^([0-9]+/)$', views.story),
]
