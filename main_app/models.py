from django.db import models
from django.urls import reverse
# Create your models here.
class Bird(models.Model):
    name= models.CharField(max_length= 100)
    species= models.CharField(max_length = 100)
    description= models.CharField(max_length= 100)
    age = models.IntegerField("How old is he/her?")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})