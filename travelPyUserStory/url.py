# customize UserBlog App URLS Routing from travelPyUserBlog

from django.conf.urls import url

from travelPyUserStory import views

urlpatterns = [
    url(r'^$', views.all),
    url(r'^new/$', views.new_story),
    url(r'^edit/(?P<story_id>\d+)/$', views.edit_story),
    url(r'^(?P<story_id>\d+)/$', views.read_story),
]
