from dataclasses import fields
from rest_framework import serializers
from .models import Building, Like, ReviewTest

class reviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        # fields = ('id', 'contents', 'recommend', 'buildingId')
        fields = "__all__"
        
class reviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = "__all__"

#동환-----------------
class BuildingListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class BuildingCreateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['name','address']

class BuildingRetireveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = ['contents', 'recommend']

class BuildingSerializeDetail(serializers.Serializer):
    building = BuildingRetireveSerializer()
    reviewList = ReviewSerializer(many=True)

class likeSerialize(serializers.Serializer):
    class Meta:
        model = Like
        fields = '__all__'