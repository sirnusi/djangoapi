from .serializers import NoteSerializer
from .models import Note
from rest_framework.response import Response

def note_list(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes)
    return Response(serializer.data)