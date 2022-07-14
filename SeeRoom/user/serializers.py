from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']

class ReviewSerializer():
    pass

class LikeSerializer():
    pass

# class ProfileSerializer(serializers.Serializer):
#     reviewList = ReviewSerializer(many=True)
#     likeList = LikeSerializer(many=True)
#     user = UserSerializer()