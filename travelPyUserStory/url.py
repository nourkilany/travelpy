# customize UserBlog App URLS Routing from travelPyUserBlog

from django.conf.urls import url

from travelPyUserStory import views

urlpatterns = [
    url(r'^city_id=(?P<city_id>\d+)/$', views.all),
    url(r'^new/city_id=(?P<city_id>\d+)/$', views.new_story),
    url(r'^edit/(?P<story_id>\d+)/$', views.edit_story),
    url(r'^(?P<story_id>\d+)/$', views.read_story),
    url(r'^(?P<story_id>\d+)/(?P<city_id>\d+)/$', views.read_story),
    #   <a href="/strories/city={{cityId}}/">
]
