from django.urls import path
from .views import *
app_name = 'review'
urlpatterns = [
    path('', reviewPostAndList.as_view()),

    path('<int:pk>/', buildingReviewListAndCreate.as_view()),
    path('<int:pk>/<int:ppk>/', reviewDetail.as_view()),

    # 동환
    path('building/', BuildingListView.as_view(), name='building-list'),    # 빌딜 리스트 페이지(필터, 조건 적용x)
    path('building/<int:pk>/', BuildingDetailView.as_view(), name='building-detail'),   # 빌딩 세부 페이지
    path('<int:pk>/recommend/', ReviewRecommend.as_view(), name='review-recommend')    # 리뷰 추천 기능
]