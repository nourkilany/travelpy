from django.db import models
from travelPyLands.models import City
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
    story_title = models.CharField(max_length = 150)
    story_body = models.TextField()
    city = models.ForeignKey('travelPyLands.City', on_delete=models.CASCADE)
    user  = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Comment(models.Model):
    user  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    story = models.ForeignKey('Story', on_delete=models.CASCADE)
    comment_body = models.TextField()

