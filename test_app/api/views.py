from test_app.api.serializers import MovieSerializer
from test_app.models import Movie
from rest_framework.response import Response

def movie_list(request):
    movies = Movie.objects.al()
    serializer = MovieSerializer(movies)
    return Response(serializer.data)
    
