from django.db import models
from travelPyLands.models import City
# Create your models here.

class Story(models.Model):
    story_title = models.CharField(max_length = 150)
    story_body = models.TextField()
    user_id  = models.IntegerField()
    city = models.ForeignKey('travelPyLands.City', on_delete=models.CASCADE)


class Comment(models.Model):
    user_id  = models.IntegerField()
    story = models.ForeignKey('Story', on_delete=models.CASCADE)
    comment_body = models.TextField()
