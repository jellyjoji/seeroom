from django.urls import path,include 
from .views import UserListAPIView
# ProfileAPIView, 
urlpatterns = [
    path('',UserListAPIView.as_view(), name='users'),
    # path('<int:pk>',ProfileAPIView.as_view(),name='profile'),
]
