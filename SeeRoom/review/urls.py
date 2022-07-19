from django.urls import path
from .views import *
app_name = 'review'
urlpatterns = [
    #전체 리뷰 리스트
    path('', reviewPostAndList.as_view()),
    path('<int:pk>/', buildingReviewListAndCreate.as_view()),#건물 리뷰리스트
    path('<int:pk>/<int:ppk>/', reviewDetail.as_view()),#리뷰 디테일

]