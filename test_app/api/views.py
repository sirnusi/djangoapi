from test_app.api.serializers import NoteSerializer
from test_app.models import Note
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class NoteList(APIView):
    
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class NoteDetail(APIView):
    def get(self, request, pk):
        notes = Note.objects.get(pk=pk)
        serializer = NoteSerializer(notes)
        return Response(serializer.data)
    
    def put(self, request, pk):
        notes = Note.objects.get(pk=pk)
        serializer = NoteSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
    def delete(self, request, pk):
        notes = Note.objects.get(pk=pk)
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        
# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
    
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'not found or you could create'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         movies = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movies, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
    
   
#     elif request.method == 'DELETE':
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    