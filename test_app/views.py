# from django.http import JsonResponse
# from .models import Movie
# # Create your views here.


# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {'movies': list(movies.values())}
#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movies = Movie.objects.get(pk=pk)
#     data = {
#         'name':movies.name,
#         'description': movies.description,
#         'active': movies.active
#     }
#     return JsonResponse(data)