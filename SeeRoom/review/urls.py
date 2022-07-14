from django.urls import path
from .views import *
app_name = 'review'
urlpatterns = [
    path('', reviewPostAndList.as_view()),

    # like update
    path('<int:pk>/', reviewDetail.as_view()),
]