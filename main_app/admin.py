from django.contrib import admin
# Register your models here.

from .models import Bird, Feeding, Photo

admin.site.register(Bird)
admin.site.register(Feeding)