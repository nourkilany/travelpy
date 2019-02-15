# customize UserBlog App URLS Routing from travelPyUserBlog

from django.conf.urls import url

from travelPyUserBlog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cities', views.cities, name='cities')
]
