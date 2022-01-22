from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerilzers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        # extra_kwargs={'password':{'write_only':True,'required':True}}
    
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model=movies
        fields=['id','title','desc','no_of_ratings','avg_ratings']

class RatingsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=ratings
        fields="__all__"