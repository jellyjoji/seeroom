import re
import django
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from .serializers import BuildingListSerialize, BuildingSerializeDetail, reviewSerialize, reviewDetailSerialize,likeSerialize, makeBuildingReviewSerialize, tempBuilding, testBuilding
from .models import Building, ReviewTest,Like
from accounts.models import User

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
class BuildingListView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingListSerialize
    def perform_create(self, serializer):
        serializer.save()


# 빌딩 id에 맞는 빌딩 정보 및 리뷰 show
class BuildingDetailView(RetrieveAPIView, CreateAPIView):
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

#건물 좋아요

#빌딩  detail 리뷰 생성
class makeReviewAtBuilding(APIView):
    queryset = ReviewTest.objects.all()
    serializer_class = makeBuildingReviewSerialize
    # def perform_create(self, serializer):
    #     print(serializer)
    #     serializer.save()
    def post(self, request, pk):   
        review_data = {'contents': request.data["reviewList.contents"], 'userId': request.user.id, 'buildingId': self.kwargs['pk'], 'recommend': 0}
        review_data_serialize = reviewSerialize(data=review_data)
        if review_data_serialize.is_valid():
            review_data_serialize.save()
        buildStar = Building.objects.get(id=self.kwargs['pk'])
        rreeview = ReviewTest.objects.filter(buildingId=self.kwargs['pk'])
        reviewCount = len(rreeview)
        build_data = {
            'moldScore': (float(request.data['building.moldScore'])+buildStar.moldScore*(reviewCount-1))/reviewCount, 
            'bugScore': (float(request.data['building.bugScore'])+buildStar.bugScore*(reviewCount-1))/reviewCount, 
            'smellScore': (float(request.data['building.smellScore'])+buildStar.smellScore*(reviewCount-1))/reviewCount, 
            'cleanAvg': buildStar.cleanAvg,
            
            'internalNoiseScore': (float(request.data['building.internalNoiseScore'])+buildStar.internalNoiseScore*(reviewCount-1))/reviewCount, 
            'externalNoiseScore': (float(request.data['building.externalNoiseScore'])+buildStar.externalNoiseScore*(reviewCount-1))/reviewCount, 
            'floorNoiseScore': (float(request.data['building.floorNoiseScore'])+buildStar.floorNoiseScore*(reviewCount-1))/reviewCount, 
            'noiseAvg': buildStar.noiseAvg, 

            'parkingScore': (float(request.data['building.parkingScore'])+buildStar.parkingScore*(reviewCount-1))/reviewCount, 
            'managementScore': (float(request.data['building.managementScore'])+buildStar.managementScore*(reviewCount-1))/reviewCount, 
            'constructionScore': (float(request.data['building.constructionScore'])+buildStar.constructionScore*(reviewCount-1))/reviewCount, 
            'locationsAvg': buildStar.locationsAvg,

            'elevator': request.data['building.elevator'], 
            'femaleOnly': request.data['building.femaleOnly'], 
            'cctv': request.data['building.cctv'], 
            'courierBox': request.data['building.courierBox'], 
            'safeAvg': buildStar.safeAvg,
            }

        build_data_serialize = tempBuilding(buildStar, data=build_data)
        review = ReviewTest.objects.filter(buildingId=self.kwargs['pk'])
        count = len(review)
        if build_data_serialize.is_valid():
            build_data_serialize.save()
            build_data_serialize = Building.objects.get(id=self.kwargs['pk'])
            cleanAvg = (build_data_serialize.cleanAvg*(count-1)+(build_data_serialize.smellScore + build_data_serialize.bugScore + build_data_serialize.moldScore)/3)/count
            noiseAvg = (build_data_serialize.noiseAvg*(count-1)+(build_data_serialize.floorNoiseScore + build_data_serialize.externalNoiseScore + build_data_serialize.internalNoiseScore)/3)/count
            locationsAvg = (build_data_serialize.locationsAvg*(count-1)+(build_data_serialize.parkingScore + build_data_serialize.managementScore + build_data_serialize.constructionScore)/3)/count
            safeAvg=(build_data_serialize.safeAvg*(count-1)+((1.25 if build_data_serialize.femaleOnly else 0.0) + (1.25 if build_data_serialize.cctv else 0.0) + (1.25 if build_data_serialize.courierBox else 0.0) + (1.25 if build_data_serialize.elevator else 0.0)))/count
            last_build = Building.objects.get(id=self.kwargs['pk'])
            last_data={"cleanAvg": cleanAvg, "noiseAvg": noiseAvg, "locationsAvg": locationsAvg, "safeAvg": safeAvg}
            last_data_serialize = testBuilding(last_build, data=last_data)
            if last_data_serialize.is_valid():
                last_data_serialize.save()
                return Response(last_data_serialize.data)
                
        # return Response(review_data)
        # return Response({'a': })
        




