from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from accounts.models import User
from user.serializers import UserSerializer
from rest_framework.response import Response
from django.http import Http404

# class MyReviewView(APIView):
#     def get_object(self, pk):# revies 객체 가져오기 
#         try:
#             return Review.objects.get(=pk)
#         except Review.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         review = self.get_object(pk)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)

class UserListAPIView(APIView):
    
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)

# class ProfileAPIView(APIView):
#     # def get_object(self, pk):# revies 객체 가져오기 
#     #     try:
#     #         return User.objects.get(pk=pk)
#     #     except User.DoesNotExist:
#     #         raise Http404
    
#     def get(self, request,pk, *args, **kwargs):
#         reviewList = get_object_or_404(Review,userID=pk)
#         likeList = get_object_or_404(Like,userID=pk)
#         user = User.objects.get(pk=pk)
#         data = {
#             'reviewList': reviewList,
#             'likeList': likeList,
#             'user' : user,
#         }

#         serializer = ProfileSerializer(instance=data)
#         return Response(serializer.data)


