from django.urls import path,include 
from .views import UsersView
# ProfileAPIView, 
urlpatterns = [
    path('',UsersView.as_view(), name='users'),
    # path('<int:pk>',ProfileAPIView.as_view(),name='profile'),

]
