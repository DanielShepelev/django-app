from django.db import models

# Create your models here
class FoodiPrefrence(models.Model):
    FoodType = models.CharField(max_length=80)
    Restrictions = models.CharField(max_length=1000)
    City = models.CharField(max_length=80)
