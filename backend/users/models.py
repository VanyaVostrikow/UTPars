from django.db import models
from services.models import Languages, Countries

class Users(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    rating = models.IntegerField()

class UserDetail(models.Model):
    user_id = models.OneToOneField(Users, primary_key=True,  on_delete=models.CASCADE)
    chat_id = models.CharField(max_length=20)
    username = models.CharField(max_length=140, null=True)
    firstname = models.CharField(max_length=140, null=True)
    lastname = models.CharField(max_length=140, null=True)
    email = models.EmailField(max_length=140, null=True)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE,null=True)
    language_id = models.ForeignKey(Languages, on_delete=models.CASCADE, null=True)
    want_recomend = models.BooleanField(null=True)
    rating = models.IntegerField(null=True)

# Create your models here.
