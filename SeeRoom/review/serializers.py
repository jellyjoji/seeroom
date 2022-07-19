from dataclasses import field
from rest_framework import serializers
from .models import ReviewTest, Building

class reviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        # fields = ('id', 'contents', 'recommend', 'buildingId')
        fields = "__all__"
        
class reviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = "__all__"
