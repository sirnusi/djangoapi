from test_app.api.serializers import MovieSerializer
from test_app.models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def movie_list(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view()   
def movie_details(request, pk):
    movies = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)