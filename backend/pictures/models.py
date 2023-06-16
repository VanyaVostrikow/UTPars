from django.db import models

class Logos(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    path = models.CharField(max_length=300)

class Thumbnail(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    path = models.CharField(max_length=300)

# Create your models here.
