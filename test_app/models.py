from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    
    def __str__(self):
        return self.title