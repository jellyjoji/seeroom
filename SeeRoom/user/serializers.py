from pyexpat import model
from rest_framework import serializers

from accounts.models import User
from review.models import ReviewTest


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = ('userId', 'contents', 'id', 'buildingId')


class ProfileSerializer(serializers.Serializer):
    reviewList = ReviewSerializer(many=True)
    # likeList = LikeSerializer(many=True)
    user = UserSerializer()
