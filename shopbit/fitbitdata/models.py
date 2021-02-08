from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


distance_hash = {385 : "Toronto", 184 : "Montreal", 482 : "Waterloo"}
# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=20)
    username = models.CharField(max_length=200)

class UserBadges(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.CharField(max_length=20)

# @receiver(post_save, sender=User)
# def create_user_badges(sender, instance, created, **kwargs):
#     if created:
#         UserBadges.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_badges(sender, instance, **kwargs):
#     instance.userbadges.save()