from django.urls import path
from . import views
from django.urls import reverse
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>', views.bird_details, name='details'),
    #creates a urlpath  for a new bird
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
]
