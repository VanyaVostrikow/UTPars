from rest_framework import serializers
from .models import Video, Video_info
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class Video(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("__all__")

class Videoinfo(serializers.ModelSerializer):
    class Meta:
        model = Video_info
        fields = ("__all__")
    

