from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import reviewSerialize, reviewDetailSerialize
from .models import ReviewTest


class reviewPostAndList(generics.ListCreateAPIView):
    queryset = ReviewTest.objects.all()
    serializer_class = reviewSerialize
    def perform_create(self, serializer):
        serializer.save(userId=self.request.user.id)
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
    def perform_create(self, serializer):
        serializer.data.userId = self.request.user.id
        serializer.save()

