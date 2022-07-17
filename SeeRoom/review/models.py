from django.db import models
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

    def __str__(self):
        return self.name

# 청결 평가 항목
class CleanlinessEvaluation(models.Model):
    moldScore = models.FloatField   # 곰팡이 점수
    bugScore = models.FloatField    # 벌레 점수
    smellScore = models.FloatField  # 냄새 점수
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE, db_column="buildingId")   # 건물 id

# 소음 평가 항목
class NoiseEvaluation(models.Model):
    internalNoiseScore = models.FloatField  # 내부소음 점수
    externalNoiseScore = models.FloatField  # 외부소음 점수
    floorNoiseScore = models.FloatField  # 층간소음 점수
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)   # 건물 id

# 위치 평가 항목
class LocationEvaluation(models.Model):
    parkingScore = models.FloatField    # 주차 점수
    managementScore = models.FloatField # 관리 점수
    constructionScore = models.FloatField   # 구축/신축 점수
    elevator = models.BooleanField  # 엘리베이터 유무 
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)   # 건물 id

# 치안 평가 항목
class SafetyEvaluation(models.Model):
    femaleOnly = models.BooleanField    # 여성전용 여부
    cctv = models.BooleanField  # cctv 유무
    courierBox = models.BooleanField    # 무인택배함 유무
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE)   # 건물 id

class ReviewTest(models.Model):
    contents = models.TextField(null=True, default='')  # 주관식
    recommend = models.PositiveIntegerField(default=0)  # 추천수
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)   # 건물 id

    name = models.CharField(max_length=200, default='') # 이름
    address = models.CharField(max_length=200, default='')  # 주소
    deposit = models.IntegerField(default=0)   # 보증금
    monthlyRent = models.IntegerField(default=0)   # 월세

    moldScore = models.IntegerField(default=0)   # 곰팡이 점수
    bugScore = models.IntegerField(default=0)    # 벌레 점수
    smellScore = models.IntegerField(default=0)  # 냄새 점수

    internalNoiseScore = models.IntegerField(default=0)  # 내부소음 점수
    externalNoiseScore = models.IntegerField(default=0) # 외부소음 점수
    floorNoiseScore = models.IntegerField(default=0)  # 층간소음 점수

    parkingScore = models.IntegerField(default=0)    # 주차 점수
    managementScore = models.IntegerField(default=0) # 관리 점수
    constructionScore = models.IntegerField(default=0)   # 구축/신축 점수
    elevator = models.BooleanField(default=False)  # 엘리베이터 유무 

    femaleOnly = models.BooleanField(default=False)    # 여성전용 여부
    cctv = models.BooleanField(default=False)  # cctv 유무
    courierBox = models.BooleanField(default=False)   # 무인택배함 유무
