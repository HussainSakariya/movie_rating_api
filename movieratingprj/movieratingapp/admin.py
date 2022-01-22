from django.contrib import admin
from .models import *
# Register your models here.

# @admin.register(movies)
# class MovieAdmin(admin.ModelAdmin):
#     fields=['title']

# @admin.register(ratings)
# class RatingsAdmin(admin.ModelAdmin):
#     fields="['ratings']"


admin.site.register(movies)
admin.site.register(ratings)