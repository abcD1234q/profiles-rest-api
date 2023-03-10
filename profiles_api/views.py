from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



# Create your views here.
class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer
   
   
   
    def get(self, request, format=None):
        an_api_view=[
            'Hare Krishna',
            'Hare Krishna',
            'Krishna Krishna',
            'Hare Hare'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_api_view})

    def post(self, request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self, request):
        a_list =[
            'Hare Rama',
            'Hare Rama',
            'Rama Rama',
            'Hare Hare'
        ]
        return Response({'message':'Hello!','a_list':a_list})   
    
    def create(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
    


class UserProfileViewSet(viewsets.ModelViewSet):
    """creating and updating users handeled"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserLogin(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)