from django.urls import path,include
from rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('join/', include('rest_auth.registration.urls'),name='join' ),
]