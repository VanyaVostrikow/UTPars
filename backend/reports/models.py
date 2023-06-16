from django.db import models
from users.models import Users, UserDetail
from channels.models import Channels

class Reports(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(Users,  on_delete=models.CASCADE,related_name='user_id')
    user_rating = models.IntegerField(null=True, blank=False)
    channel_id = models.ForeignKey(Channels, on_delete=models.CASCADE, blank=False, null=True,related_name='channel_id')
# Create your models here.
