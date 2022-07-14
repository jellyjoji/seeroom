from rest_framework import serializers
from .models import ReviewTest

class reviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = ('id', 'contents',)

class reviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = "__all__"