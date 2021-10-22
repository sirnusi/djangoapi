from .serializers import NoteSerializer
from .models import Note
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def note_list(request):
    
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk):
    
    if request.method == 'GET':
        notes = Note.objects.get(pk=pk)
        serializer = NoteSerializer(notes)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        notes = Note.objects.get(pk=pk)
        serializer = NoteSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        notes = Note.objects.get(pk=pk)
        notes.delete()
        return Response()