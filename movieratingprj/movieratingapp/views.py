from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import*
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class=UserSerilzers
    queryset=User.objects.all()

class MoviesViewset(viewsets.ModelViewSet):
    serializer_class=MovieSerilizer
    queryset=movies.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

class RatingsViewset(viewsets.ModelViewSet):
    serializer_class=RatingsSerilizer
    queryset=ratings.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    @action(detail=True,methods=["POST","GET"])    
    def get_ret(self,request,pk=None):
        # print("hello",request.data)
        if 'ratings' in request.data:
            movie=movies.objects.get(id=1)
            print("User",request.user)
            try:
                obj=ratings.objects.get(id=pk)
                obj.ratings=request.data['ratings']
                obj.save()
                serializer=RatingsSerilizer(obj,many=False)
                response={'message':'Update run'+str(request.data),'results':serializer.data}
                return Response(response,status=status.HTTP_200_OK)
            except:
                obj=ratings.objects.create(movie=movie,user=user,ratings=request.data['ratings'])
                serializer=RatingsSerilizer(obj,many=False)
                response={'message':'Create run'+str(request.data),'results':serializer.data}
                return Response(response,status=status.HTTP_200_OK)
            # response={'message':request}
            
        else:
            response={'message':'else run'+str(request.data)}
            # response={'message':request}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)