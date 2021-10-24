from django.contrib import admin
from .models import StreamPlatform, WatchList, Review
# Register your models here.

admin.site.register((StreamPlatform, WatchList, Review))