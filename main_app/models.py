from django.db import models

# Create your models here.
class Bird(models.Model):
    name= models.CharField(max_length= 100)
    species= models.CharField(max_length = 100)