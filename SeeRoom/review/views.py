from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from .serializers import reviewSerialize, buildingSerializeDetail
from .models import ReviewTest


class reviewPostAndList(generics.ListCreateAPIView):
    queryset = ReviewTest.objects.all()
    serializer_class = reviewSerialize

class BuildingDetailView(RetrieveAPIView):
    queryset = ReviewTest.objects.all()
    serializer_class = buildingSerializeDetail
    
