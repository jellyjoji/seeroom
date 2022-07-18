from rest_framework import serializers
from .models import ReviewTest

class reviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = ('contents', 'buildingId', 'deposit', 'monthlyRent', 'moldScore', 'bugScore', 'smellScore', 'internalNoiseScore', 'externalNoiseScore', 'floorNoiseScore', 'parkingScore', 'managementScore', 'constructionScore', 'elevator', 'femaleOnly', 'cctv', 'courierBox')

class reviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = "__all__"


# 리뷰 리스트 
# 평점 
# 빌딩
#class buildingSerializeDetail(serializers.ModelSerializer):