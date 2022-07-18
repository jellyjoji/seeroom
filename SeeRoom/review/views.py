from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from .serializers import reviewSerialize, reviewDetailSerialize
from .models import Building, ReviewTest


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

# 동환-----------------------
# 빌딩 id에 맞는 빌딩 정보 및 리뷰 show
class buildingDetail(RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializerDetail

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        cleanlinessEvaluation = instance.cleanlinessEvaluation_set.all()
        noiseEvaluation = instance.noiseEvaluation_set.all()
        locationEvaluation = instance.locationEvaluation_set.all()
        safetyEvaluation = instance.safetyEvaluation_set.all()
        data = {
            'building': instance,
            'cleanlinessEvaluation': cleanlinessEvaluation,
            'noiseEvaluation': noiseEvaluation,
            'locationEvaluation': locationEvaluation,
            'safetyEvaluation': safetyEvaluation,
        }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)

# 필터 및 조건에 맞는 빌딩 리스트 show
