from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length  = 200) 


class City(models.Model):
    city_name = models.CharField(max_length = 200)
    country = models.ForeignKey('Country',on_delete=models.CASCADE)
