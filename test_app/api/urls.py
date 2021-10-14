from django.urls import path
from test_app.api import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('details/<int:pk>/', views.MovieDetail.as_view(), name='movie_details'),
]