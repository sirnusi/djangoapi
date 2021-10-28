#Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.serializers import RegistrationSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)