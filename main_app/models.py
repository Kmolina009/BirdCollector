from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D','Dinner'), 
)
class Photo(model.Models):
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"

class Toy(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk' : self.id})
#Toy model must be place before the cat model, since the Cat model will be call "Toy"

class Bird(models.Model):
    name= models.CharField(max_length= 100)
    species= models.CharField(max_length = 100)
    description= models.CharField(max_length= 100)
    age = models.IntegerField("How old is he/her?")
    toys = models.ManyToManyField(Toy)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        #sets the default to breakfast
        default=MEALS[0][0]
    )
    #Another one to many idea would be if the bird had flights
        #bird_id foreign id
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']