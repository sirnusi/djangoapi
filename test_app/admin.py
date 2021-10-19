from django.contrib import admin
from .models import Note, Category, Review
# Register your models here.

admin.site.register((Note, Category, Review))