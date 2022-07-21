from django.urls import path
from .views import *
app_name = 'review'
urlpatterns = [
    #전체 리뷰 리스트
    path('', reviewPostAndList.as_view()),
    path('<int:pk>/', buildingReviewListAndCreate.as_view()),#건물 리뷰리스트
    path('<int:pk>/<int:ppk>/', reviewDetail.as_view()),#리뷰 디테일
  
    # 동환
    path('building/', BuildingListView.as_view(), name='building-list'),    # 빌딜 리스트 페이지(필터, 조건 적용x)
    path('building/<int:pk>/', BuildingDetailView.as_view(), name='building-detail'),   # 빌딩 세부 페이지
    path('<int:pk>/recommend/', ReviewRecommend.as_view(), name='review-recommend'),    # 리뷰 추천 기능

    # path('building/<int:pk>/like', BuildingLikeView.as_view(), name='building-like'),   # 빌딩 좋아요기능 
]