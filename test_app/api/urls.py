from django.urls import path
from test_app.api import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='note-list'),
    path('details/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    path('notes/<int:pk>/reviews', views.ReviewDetail.as_view(), name='review-detail'),
    path('notes/reviews/<int:pk>', views.ReviewList.as_view(), name='review-list'),
]