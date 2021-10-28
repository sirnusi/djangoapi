from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app import views


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.RegisterUser.as_view(), name='register')
]