from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
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
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.rating} || {self.watchlist.title} || {str(self.owner)}'