from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    event_street_address = models.CharField(max_length=200)
    event_city = models.CharField(max_length=200)
    event_zipcode = models.IntegerField()
    is_outdoors = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    has_high_pollen = models.BooleanField(default=False)

    def __str__(self):
        return "Event: %s, Attendees:<WIP>" % self.event_name


'''
ToDo for Models: 
    Establish relationship between Event and Users, probably manyToMany
    Start_time and End_Time are verifiable times in the future
    
'''
