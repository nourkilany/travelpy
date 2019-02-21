from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from travelPyLands.models import Poi

class CarRental(models.Model):
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey('travelPyLands.Poi', on_delete=models.CASCADE)
    from_date = models.DateTimeField(default=datetime.now)
    to_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.pickup_location
