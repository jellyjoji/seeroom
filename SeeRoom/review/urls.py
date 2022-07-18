from django.urls import path
from .views import *
app_name = 'review'
urlpatterns = [
    path('', reviewPostAndList.as_view()),

    
    # 동환 - 한 건물의 평점 및 리뷰 리스트
    path('<int:pk>/', BuildingDetailView.as_view(), name='review-detail'),
    # 동환 - 리뷰 좋아요
    #path('<int:pk>/like', reviewDetail.as_view(), name='review-like'),
    # 동환 - 건물 리스트

]