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
    deposit = models.IntegerField   # 보증금
    monthlyRent = models.IntegerField   # 월세
    photo = models.ImageField(blank=True, null=True)    # 사진

    #청결
    moldScore = models.FloatField   # 곰팡이 점수
    bugScore = models.FloatField    # 벌레 점수
    smellScore = models.FloatField  # 냄새 점수
    cleanAvg = models.FloatField # 청결 평균

    #소음
    internalNoiseScore = models.FloatField  # 내부소음 점수
    externalNoiseScore = models.FloatField  # 외부소음 점수
    floorNoiseScore = models.FloatField  # 층간소음 점수
    noiseAvg= models.FloatField #소음 평균

    # 위치 
    parkingScore = models.FloatField    # 주차 점수
    managementScore = models.FloatField # 관리 점수
    constructionScore = models.FloatField   # 구축/신축 점수
    elevator = models.BooleanField  # 엘리베이터 유무 
    locationsAvg = models.FloatField # 위치평균

    # 치안
    femaleOnly = models.BooleanField    # 여성전용 여부
    cctv = models.BooleanField  # cctv 유무
    courierBox = models.BooleanField    # 무인택배함 유무
    safeAvg = models.FloatField # 치안평균
    def __str__(self):
        return self.name

#리뷰
class ReviewTest(models.Model):
    contents = models.TextField(null=True,blank=True, default='')  # 주관식
    recommend = models.PositiveIntegerField(default=0)  # 추천수
    buildingId = models.ForeignKey(Building, blank=True, null=True, on_delete=models.CASCADE)   # 건물 id
    userId = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,default="") # 작성자 id

#찜
class Like(models.Model):
    buildingId = models.ForeignKey(Building, blank=True, null=True,on_delete=models.CASCADE)   # 건물 id
    userId = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE) # 작성자 id