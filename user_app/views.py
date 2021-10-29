#Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app.serializers import RegistrationSerializer
from user_app import models


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successfull.'
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            return serializer.errors
        return Response(serializer.data)