from django.db import models
from services.models import Languages, Countries

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=140, null=True, blank=False)
    firstname = models.CharField(max_length=140, null=True,blank=False)
    lastname = models.CharField(max_length=140, null=True,blank=False)
    email = models.EmailField(max_length=140, null=True,blank=False)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE,null=True)
    language_id = models.ForeignKey(Languages, on_delete=models.CASCADE, null=True)
    want_recomend = models.BooleanField(null=True,blank=False)
    date_change = models.DateTimeField(auto_now=True)
    date_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True,blank=False)


# Create your models here.
