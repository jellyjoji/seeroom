from django.urls import path
from .views import *
app_name = 'review'
urlpatterns = [
    path('', reviewPostAndList.as_view()),

    path('<int:pk>/', buildingReviewListAndCreate.as_view()),
    path('<int:pk>/<int:ppk>/', reviewDetail.as_view()),

    # 동환
    # 빌딩 id에 맞는 빌딩 정보 및 리뷰 show
    path('show/<int:pk>/', buildingDetail.as_view()),
]