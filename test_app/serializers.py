from django.db.models import fields
from rest_framework import serializers
from .models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"
    
    def get_len_name(self, object):
        return len(object.title)

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"