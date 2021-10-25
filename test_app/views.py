from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from test_app.models import WatchList, StreamPlatform, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
    
    
class StreamPlatformList(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    
class StreamPlatformDetail(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    
class WatchListAV(ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
class WatchDetail(RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer