from django.db import models
from django.db.models.fields import CharField
from fitbitdata.models import User

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)