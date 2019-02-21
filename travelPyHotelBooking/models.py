from django.db import models
from travelPyLands.models import City, Hotel
from django.contrib.auth.models import User
# Create your models here.

class HotelReservation(models.Model):
    hotel = models.CharField(max_length  = 200)
    city  = models.ForeignKey('travelPyLands.City', on_delete=models.CASCADE)
    user  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    check_in_date    = models.DateTimeField()
    check_out_date   = models.DateTimeField()
    number_of_adults = models.IntegerField()
