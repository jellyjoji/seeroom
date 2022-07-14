from django.db import models
# Create your models here.
class ReviewTest(models.Model):
    contents = models.TextField(null=True, default='')
    recommend = models.IntegerField(default=0)
    # buildings -> Foreign key