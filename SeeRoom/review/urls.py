from django.urls import path
from .views import *
app_name = 'review'
urlpatterns = [
    path('', reviewPostAndList.as_view()),

    path('<int:pk>/', buildingReviewListAndCreate.as_view()),
    path('<int:pk>/<int:ppk>/', reviewDetail.as_view()),
]