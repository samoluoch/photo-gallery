from django.db import models

# Create your models here.
class Location(models.Model):
    district = models.CharField(max_length =30)
    county = models.CharField(max_length =30)
    country = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField( max_length=100 )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True)
    # mptt.register(Category)