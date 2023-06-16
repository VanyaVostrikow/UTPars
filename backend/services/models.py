from django.db import models

class Genres(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    ganre = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, blank=False, null=True)
class Countries(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    country_name = models.CharField(max_length=100)

class Languages(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    language = models.CharField(max_length=100)

class TimeLine(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    time = models.TimeField()

class Templates(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=100)
    language_id = models.ForeignKey(Languages, on_delete=models.CASCADE )

class Errors(models.Model):
    code = models.IntegerField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=200)
    text = models.CharField(max_length=1024)





# Create your models here.
