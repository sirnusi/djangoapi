from .models import Note
from django.http import JsonResponse

def note_list(request):
    notes = Note.objects.all()
    data = {'movies': list(notes.values())}
    return JsonResponse(data)

def note_detail(request, pk):
    notes = Note.objects.get(pk=pk)
    data = {
        'title': notes.title,
        'description': notes.description,
    }
    return JsonResponse(data)