from django.contrib.auth.models import User
from rest_frameworks import Response
from rest_framework.generics import CreateAPIView
from .serializers import RegistrationSerializer

# Create your views here.
class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    
    