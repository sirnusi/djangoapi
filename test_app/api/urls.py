from django.urls import path
from test_app.api import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='movie_list'),
    path('details/<int:pk>/', views.NoteDetail.as_view(), name='movie_details'),
]