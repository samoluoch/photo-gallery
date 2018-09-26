from django.db import models

# Create your models here.
class Location(models.Model):
    district = models.CharField(max_length =30)
    county = models.CharField(max_length =30)
    country = models.CharField(max_length=30)