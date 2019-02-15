from django.db import models

# Create your models here.


class Cities(models.Model):

    cityCountry = models.CharField(max_length=6)
    cityName = models.CharField(max_length=150)
    cityRate = models.IntegerField(default=0)
    cityLatitude = models.FloatField(default=0.0)
    cityLongitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.cityName


