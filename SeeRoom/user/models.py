from django.db import models
from accounts.models import User
from review.models import Building

# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         to= User, on_delete=models.CASCADE, primary_key=True
#     )
#     bookmark = models.ManyToManyField("Building")
#     reviewList = models.ManyToOneRel