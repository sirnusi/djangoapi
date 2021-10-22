from django.db.models import fields
from rest_framework import serializers
from .models import WatchList, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"