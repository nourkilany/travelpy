from django.db import models

# Create your models here.
class Continent(models.Model):
    continent_name = models.CharField(max_length=50)
    sygic_id      = models.CharField(blank=True,null=True,max_length  = 50) 

    def __str__(self):
        return self.continent_name


class Country(models.Model):
    country_name  = models.CharField(max_length  = 200) 
    sygic_id      = models.CharField(blank=True,null=True,max_length  = 50) 
    country_perex = models.TextField( blank=True,null=True)
    country_desc  = models.TextField( blank=True,null=True)
    country_lat   = models.FloatField( blank=True,null=True)
    country_lng   = models.FloatField( blank=True,null=True)
    country_rate  =  models.DecimalField(  blank=True,null=True, max_digits=11, decimal_places=10) #--> rating local !!
    country_low_image = models.CharField(  blank=True,null=True, max_length = 400)
    country_high_image = models.CharField(  blank=True,null=True, max_length = 400)
    continent     = models.ForeignKey('Continent', on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name  = models.CharField(max_length  = 200) 
    sygic_id      = models.CharField(blank=True,null=True,max_length  = 50) 
    city_perex = models.TextField( blank=True,null=True)
    city_desc  = models.TextField( blank=True,null=True)
    city_lat   = models.FloatField( blank=True,null=True)
    city_lng   = models.FloatField( blank=True,null=True)
    city_rate  = models.DecimalField(  blank=True,null=True, max_digits=11, decimal_places=10) #--> rating local !!
    city_low_image = models.CharField(  blank=True,null=True, max_length = 400)
    city_high_image = models.CharField(  blank=True,null=True, max_length = 400)
    country = models.ForeignKey('Country',on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Poi(models.Model):
    poi_name  = models.CharField(max_length  = 200)
    sygic_id      = models.CharField(blank=True,null=True,max_length  = 50) 
    poi_perex = models.TextField( blank=True,null=True)
    poi_desc  = models.TextField( blank=True,null=True)
    poi_lat   = models.FloatField( blank=True,null=True)
    poi_lng   = models.FloatField( blank=True,null=True)
    poi_rate  = models.DecimalField(  blank=True,null=True, max_digits=11, decimal_places=10) # --> rating local !!
    poi_low_image = models.CharField(  blank=True,null=True, max_length = 400)
    poi_high_image = models.CharField(  blank=True,null=True, max_length = 400)
    city = models.ForeignKey('City',on_delete=models.CASCADE)

    def __str__(self):
        return self.poi_name
