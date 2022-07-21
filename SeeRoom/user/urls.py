from django.urls import path,include 
from .views import UserListAPIView, UserReviewListAPI,ProfileAPIView
# ProfileAPIView, 
urlpatterns = [
    path('',UserListAPIView.as_view(), name='users'),
    path('<int:pk>',ProfileAPIView.as_view(),name='profile'),
    path('reviews/', UserReviewListAPI.as_view()),
]
