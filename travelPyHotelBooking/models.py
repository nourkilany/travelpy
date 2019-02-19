from django.db import models
from travelPyLands.models import City

# Create your models here.
class Hotel(models.Model):
    hotel_name  = models.CharField(max_length  = 200) 
    hotel_perex = models.TextField()
    hotel_desc  = models.TextField()
    hotel_lat   = models.FloatField()
    hotel_lng   = models.FloatField()
    hotel_rate  = models.DecimalField(max_digits=11, decimal_places=10) # --> rating local !!
    hotel_low_image = models.CharField(max_length = 400)
    hotel_high_image = models.CharField(max_length = 400)
    city = models.ForeignKey('travelPyLands.City', on_delete=models.CASCADE)

    def __str__(self):
        return self.poi_name
    