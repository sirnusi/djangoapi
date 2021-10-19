from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    time_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='reviews')
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.rating
