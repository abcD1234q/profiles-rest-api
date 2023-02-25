from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    def get(self, request, format=None):
        an_api_view=[
            'Hare Krishna',
            'Hare Krishna',
            'Krishna Krishna',
            'Hare Hare'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_api_view})