from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class CarRentalForm(models.Model):
    
    user_id = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    pickup_location = models.CharField(max_length=50)
    from_date = models.DateTimeField(default=datetime.now)
    to_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.pickup_location
