from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register('movies', MoviesViewset)
router.register('ratings', RatingsViewset)
router.register('users', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]
