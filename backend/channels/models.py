from django.db import models
from users.models import Users
from pictures.models import Logos

class Channels(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=666)
    link = models.CharField(max_length=666)
    shortlink = models.CharField(max_length=100, null=True, blank=False)
    logo_id = models.ForeignKey(Logos, on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=666)
    rating = models.IntegerField()

class Subscribe(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(Users,  on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channels,  on_delete=models.CASCADE)

# Create your models here.
