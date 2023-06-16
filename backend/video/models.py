from django.db import models
from channels.models import Channels
from pictures.models import Thumbnail
from services.models import Genres


class Video_info(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=250)
    thumbnail_id = models.ForeignKey(Thumbnail,  on_delete=models.CASCADE)
    date_create = models.DateField()

class Video(models.Model):
    video_id = models.OneToOneField(Video_info, primary_key=True,  on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channels, on_delete=models.CASCADE,null=True)
    genre_id = models.ForeignKey(Genres,  on_delete=models.CASCADE,null=True)

# Create your models here.
