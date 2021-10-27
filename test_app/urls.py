from django.urls import path
from test_app import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', views.WatchDetail.as_view(), name='watch-detail'),
    path('stream/', views.StreamPlatformList.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>/', views.StreamPlatformDetail.as_view(), name='streamplatform-detail'),
    # path('reviews/', views.ReviewList.as_view(), name='review-list'),
    # path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail')
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'), # pk is for the actual movie you want to review on
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'), # list out all the reviews for a particular movie
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'), # access individual review to update, destroy, retrieve
    
]