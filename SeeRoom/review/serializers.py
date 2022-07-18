from rest_framework import serializers
from .models import ReviewTest

class reviewSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = "__all__"
        
class reviewDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = ReviewTest
        fields = "__all__"