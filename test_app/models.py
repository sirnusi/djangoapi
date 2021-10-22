from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=25)
    about = models.CharField(max_length=100)
    website = models.URLField()
    
    def __str__(self):
        return f'{self.name}'

class WatchList(models.Model):
    title = models.CharField(max_length=25)
    storyline = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'