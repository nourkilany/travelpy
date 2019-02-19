from django.db import models
from datetime import datetime
# TODO : don't forget to import User model when created
class CarRentalForm(models.Model):
    # * I assumed that the Model Class for the user is namd User as it is not
    # * yet created so I'm going to comment it to avoid errors for now
     
    #user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pickup_location = models.CharField(max_length=50)
    from_date = models.DateTimeField(default=datetime.now)
    to_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.pickup_location
