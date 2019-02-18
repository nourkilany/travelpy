from django.db import models

# Create your models here.
class Country(models.Model):

    country_name = models.CharField(max_length  = 200) 
    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length = 200)
    country = models.ForeignKey('Country',on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Continent(models.Model):
    continent_name = models.CharField(max_length=50)

    def __str__(self):
        return self.continent_name
