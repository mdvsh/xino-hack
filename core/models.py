from django.db import models
from django.contrib.auth.models import User

class Places(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class InterestsActivities(models.Model):
    name = models.CharField(max_length=100)

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isGuide = models.BooleanField(default=False)
    places_of_interest = models.ManyToManyField(Places, related_name='user_places_of_interest')
    interests = models.ManyToManyField(InterestsActivities, related_name='InterestsActivities')

class Hiring(models.Model):
    traveller = models.ForeignKey(CustomUser, related_name='hiring_traveller', on_delete=models.SET_NULL, null=True)
    guide = models.ForeignKey(CustomUser, related_name='hiring_guide', on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Places, related_name='hiring_place', on_delete=models.SET_NULL, null=True)
    pay = models.FloatField(null=True)