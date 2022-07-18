from rest_framework import serializers
from .models import ReviewTest

class reviewListSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = ['contents', 'recommend']


# 리뷰 리스트 
# 평점 
# 빌딩
#class buildingSerializeDetail(serializers.ModelSerializer):