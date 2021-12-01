from . import serializers, models
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# class StreamPlatformTestCase(APITestCase):
    
#     def setUp(self):
#         self.user = User.objects.create(username='example', password='NewPassword')
#         self.token = Token.objects.get(user__username=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
#     def test_streamplatform_create(self):
#         data = {
#             'name': 'Netflix',
#             'about': '#1 in the World.',
#             'website': 'https://netflix.com'
#         }
#         response = self.client.post(reverse('streamplatform-list'), data)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)