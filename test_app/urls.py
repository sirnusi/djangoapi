from django.urls import path
from test_app import views

urlpatterns = [
    path('list/', views.note_list, name='movie-list'),
    path('detail/<int:pk>/', views.note_detail, name='movie-detail')
]