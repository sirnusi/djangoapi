from .serializers import WatchListSerializer, StreamPlatformSerializer
from test_app.models import WatchList, StreamPlatform
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class StreamPlatformList(APIView):
    
    def get(self, request):
        stream_platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream_platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
class StreamPlatformDetail(APIView):
    
    def get(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        stream_platform.delete()
        return Response(status=status.HTTP_204_DELETED)

class WatchListAV(APIView):
    
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class WatchDetail(APIView):
    
    def put(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlist)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
           watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'WatchList Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    

    def delete(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

