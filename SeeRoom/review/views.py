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

    

<<<<<<< HEAD
# 올리기 연습용 주석
=======
>>>>>>> 5ed01a24f9d811862960e6f6460a79217363ce24
