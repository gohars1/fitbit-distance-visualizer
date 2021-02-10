from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

distance_hash = {385 : "Toronto", 184 : "Montreal", 482 : "Waterloo", 384400 : "Moon" }
floors_hash = {147 : "CN Tower", 102 : "Empire State", 2061: "Mount Everest" , 2309: "Ascension"}


# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=200)
    life_time_km = models.IntegerField(default=0)
    life_time_floors = models.IntegerField(default=0)

class UserBadges(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    badge = models.CharField(max_length=20)



#
#   badges page:
#
#   badge 1  share
#   badge 2  share
#   badge 3  share
#   badge 4 In progress
#   badge 5 In progress
#
#
#
#