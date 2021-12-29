from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from test_app.models import WatchList, StreamPlatform, Review
from .permissions import AdminOrReadOnly, ReviewOwnerOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from test_app.throttling import ReviewCreateThrottle, ReviewListThrottle
from test_app.pagination import WatchListPagination, WatchListCursorPagination

class UserReview(ListAPIView):
    serializer_class = ReviewSerializer
    
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(owner__username=username)
    
    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Review.objects.filter(owner__username=username)
    

class ReviewCreate(CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        owner = self.request.user
        owner_queryset = Review.objects.filter(watchlist=watchlist, owner=owner)
        
        if owner_queryset.exists():
            raise ValidationError("You have reviewed this movie!")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2
        
        watchlist.number_rating += 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, owner=owner)
class ReviewList(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner__username', 'active']

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
    permission_classes = [ReviewOwnerOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
    
    
class StreamPlatformList(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [AdminOrReadOnly]
    
class StreamPlatformDetail(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [AdminOrReadOnly]

class WatchListSearch(ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    # filter_backends = [filters.SearchFilter]
    
    # filter_backends = [filters.OrderingFilter]
    
    # search_fields = ['title', 'platform__name']
    
    # ordering_fields = ['avg_rating']
    
    pagination_class = WatchListCursorPagination
    

class WatchListAV(ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [AdminOrReadOnly]
    
class WatchDetail(RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [AdminOrReadOnly]