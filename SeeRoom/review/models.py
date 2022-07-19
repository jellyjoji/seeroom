from django.db import models
from accounts.models import User
# Create your models here.
# class ReviewTest(models.Model): 이부분 없애 주세요
#     contents = models.TextField(null=True, default='')
#     recommend = models.PositiveIntegerField(default=0)

# 건물 정보
class Building(models.Model):
    name = models.CharField(max_length=200) # 이름
    address = models.CharField(max_length=200)  # 주소

    deposit = models.IntegerField(blank=True, null=True)  # 보증금
    monthlyRent = models.IntegerField(blank=True, null=True)   # 월세
    photo = models.ImageField(blank=True, null=True)    # 사진

    #청결
    moldScore = models.FloatField(blank=True, null=True)   # 곰팡이 점수
    bugScore = models.FloatField(blank=True, null=True)    # 벌레 점수
    smellScore = models.FloatField(blank=True, null=True)  # 냄새 점수
    cleanAvg = models.FloatField(blank=True, null=True) # 청결 평균

    #소음
    internalNoiseScore = models.FloatField(blank=True, null=True)  # 내부소음 점수
    externalNoiseScore = models.FloatField(blank=True, null=True)  # 외부소음 점수
    floorNoiseScore = models.FloatField(blank=True, null=True)  # 층간소음 점수
    noiseAvg= models.FloatField(blank=True, null=True) #소음 평균

    # 위치 
    parkingScore = models.FloatField(blank=True, null=True)    # 주차 점수
    managementScore = models.FloatField(blank=True, null=True) # 관리 점수
    constructionScore = models.FloatField(blank=True, null=True)   # 구축/신축 점수
    elevator = models.BooleanField(blank=True, null=True)  # 엘리베이터 유무 
    locationsAvg = models.FloatField(blank=True, null=True) # 위치평균

    # 치안
    femaleOnly = models.BooleanField(blank=True, null=True)    # 여성전용 여부
    cctv = models.BooleanField(blank=True, null=True)  # cctv 유무
    courierBox = models.BooleanField(blank=True, null=True)    # 무인택배함 유무
    safeAvg = models.FloatField(blank=True, null=True) # 치안평균
    
    def __str__(self):
        return self.name

#리뷰
class ReviewTest(models.Model):
    contents = models.TextField(null=True,blank=True, default='')  # 주관식
    recommend = models.PositiveIntegerField(default=0)  # 추천수
    buildingId = models.ForeignKey(Building, blank=True, null=True, on_delete=models.CASCADE)   # 건물 id
    userId = models.IntegerField(blank=True, null=True,default=None) # 작성자 id


#찜
# class Like(models.Model):
#     buildingId = models.ForeignKey(Building, blank=True, null=True,on_delete=models.CASCADE)   # 건물 id
#     userId = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE) # 작성자 idp