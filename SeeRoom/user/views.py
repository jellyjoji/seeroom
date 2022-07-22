from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from accounts.models import User
from user.serializers import UserSerializer, ReviewSerializer,ProfileSerializer
from rest_framework.response import Response
from rest_framework import generics, serializers
from review.models import ReviewTest


class UserListAPIView(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

class UserReviewListAPI(generics.ListAPIView): #내가쓴글
    serializer_class = ReviewSerializer
    def get_queryset(self):
        user = self.request.user.id
        return ReviewTest.objects.filter(userId=user)

class ProfileAPIView(APIView): # 프로필 
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=self.request.user.id)
        reviewList = ReviewTest.objects.filter(userId=self.request.user.id)
        data = {
            'user': user,
            'reviewList': reviewList,
        }

        serializer = ProfileSerializer(instance=data)
        return Response(serializer.data)
