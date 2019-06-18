from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird, Toy, Photo
import uuid
import boto3
from .forms import FeedingForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'birdcollector009'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds':birds })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id =  bird_id)
    toys_cat_doesnt_have= Toy.objects.exclude(id_in= cat.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html',{ 'bird' : bird, 'feeding_form:': feeding_form, 
    'toys': toys_bird_doesnt_have
    })

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('detail', bird_id=bird_id)

def assoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('detail', cat_id=cat_id)

def add_photo(request, cat_id):
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, cat_id=cat_id)
            photo.save()
        except:
            print('An error occured uploading file to S3')
    return redirect('detail', cat_id=cat_id)

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    success_url = '/birds/'

class BirdUpdate(UpdateView):
    models = Bird
    fields=['species', 'description', 'age']

class BirdDelete(DeleteView):
    models = Bird
    success_url= '/birds/'