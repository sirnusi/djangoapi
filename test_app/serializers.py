from django.db.models import fields
from rest_framework import serializers
from .models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    # watchlist = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ['watchlist']
class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(read_only=True, many=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"