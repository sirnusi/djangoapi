from django.urls import path
from test_app import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', views.WatchDetail.as_view(), name='watch-detail'),
    path('streams/', views.StreamPlatformList.as_view(), name='streamplatform-list'),
    path('streams/<int:pk>/', views.StreamPlatformDetail.as_view(), name='streamplatform-detail')
]