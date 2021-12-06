from django.http import response
from . import serializers, models
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from . import models

class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='example', password='NewPassword')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name='Netflix', about='#1 in the World', 
                                                           website='https://netflix.com')
        
    def test_streamplatform_create(self):
        data = {
            'name': 'Netflix',
            'about': '#1 in the World.',
            'website': 'https://netflix.com'
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_streamplatform_update(self):
        response = self.client.put(reverse('streamplatform-detail', args=(self.stream.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_delete(self):
        response = self.client.delete(reverse('streamplatform-detail', args=(self.stream.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='example', password='Password123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name='ROK', about='Just 9ja', website='https://rok.com')
        self.watchlist = models.WatchList.objects.create(title='New Guy', storyline='Wonderful Movie!!!',
                                                        platform=self.stream,
                                                        active=False)
    
    def test_watchlist_create(self):
        data = {
            'title':'New Guy',
            'storyline': 'Wonderful Movie!!!',
            'platform': self.stream,
            'active': False,
        }
        response = self.client.post(reverse('watch-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_list(self):
        response = self.client.get(reverse('watch-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_detail(self):
        response = self.client.get(reverse('watch-detail', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_update(self):
        response = self.client.put(reverse('watch-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_delete(self):
        response = self.client.delete(reverse('watch-detail', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='example', password='NewPassword123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name='Netflix', about='#1 in the World', 
                                                           website='https://netflix.com')
        self.watchlist = models.WatchList.objects.create(title='Wonderland', storyline='About Harry Potter',
                                                        platform=self.stream, active=False)
        self.watchlist2 = models.WatchList.objects.create(title='Wonderland', storyline='About Harry Potter',
                                                        platform=self.stream, active=False)
        
        self.review = models.Review.objects.create(owner=self.user, rating=4, description='Just in Awe!',
                                                   active=True, watchlist=self.watchlist2)
        
    def test_review_create(self):
        data = {
            'owner': self.user,
            'rating':4,
            'description': 'Stupid Movie!!!',
            'watchlist': self.watchlist,
            'active': True
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(models.WatchList.objects.get().title, 'Wonderland')
    
    def test_create_unauth(self):
        data = {
            'owner': self.user,
            'rating':4,
            'description': 'Stupid Movie!!!',
            'watchlist': self.watchlist,
            'active': True
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_review_detail(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_update(self):
        data = {
            'owner': self.user,
            'rating':3,
            'description': 'Stupid Movie!!! - Updated',
            'watchlist': self.watchlist,
            'active': False
        }
        response = self.client.put(reverse('review-detail', args=(self.review.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id, )))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_review_user(self):
        response = self.client.get('/watch/stream/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)