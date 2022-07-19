from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView
from .serializers import BuildingListSerialize, BuildingSerializeDetail, reviewSerialize, reviewDetailSerialize
from .models import Building, ReviewTest


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

# 동환-----------------------

# 필터 및 조건에 맞는 빌딩 리스트 show
class BuildingListView(ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingListSerialize


# 빌딩 id에 맞는 빌딩 정보 및 리뷰 show
class BuildingDetailView(RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializeDetail

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        reviewList = instance.reviewtest_set.all()
        data = {
            'building': instance,
            'reviewList': reviewList
        }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)

# 리뷰 좋아요
class ReviewRecommend(GenericAPIView):
    queryset = ReviewTest.objects.all()

    # Patch method
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.recommend += 1
        instance.save()
            
        return Response(instance.recommend)


