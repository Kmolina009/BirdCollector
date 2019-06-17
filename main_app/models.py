from django.db import models
from django.urls import reverse
# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D','Dinner'),
)

class Bird(models.Model):
    name= models.CharField(max_length= 100)
    species= models.CharField(max_length = 100)
    description= models.CharField(max_length= 100)
    age = models.IntegerField("How old is he/her?")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        #sets the default to breakfast
        default=MEALS[0][0]
    )
        #bird_id foreign id
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.get_meal_display()} on {self.date}"

       #figure out the issue with this program