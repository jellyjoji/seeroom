from django.shortcuts import render
from rest_framework import generics
from .serializers import reviewSerialize, reviewDetailSerialize
from .models import ReviewTest


class reviewPostAndList(generics.ListCreateAPIView):
    queryset = ReviewTest.objects.all()
    serializer_class = reviewSerialize

class reviewDetail(generics.RetrieveUpdateAPIView):
    queryset = ReviewTest.objects.all()
    serializer_class = reviewDetailSerialize

    

