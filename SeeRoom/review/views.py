from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import reviewSerialize, reviewDetailSerialize
from .models import ReviewTest


class reviewPostAndList(generics.ListCreateAPIView):
    queryset = ReviewTest.objects.all()
    serializer_class = reviewSerialize
   
# 빌딩 id에 맞는 리뷰의 상세
class reviewDetail(generics.RetrieveUpdateAPIView):
    serializer_class = reviewDetailSerialize
    def get_queryset(self):
        return ReviewTest.objects.filter(buildingId=self.kwargs['pk'])

# 빌딩 id에 맞는 리뷰 리스트 show, create
class buildingReviewListAndCreate(generics.ListCreateAPIView):
    serializer_class = reviewSerialize
    def get_queryset(self):
        return ReviewTest.objects.filter(buildingId=self.kwargs['pk'])
