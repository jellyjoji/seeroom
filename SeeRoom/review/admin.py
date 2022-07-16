from django.contrib import admin
from .models import ReviewTest, Building, CleanlinessEvaluation, NoiseEvaluation, LocationEvaluation, SafetyEvaluation

admin.site.register(ReviewTest)
admin.site.register(Building)