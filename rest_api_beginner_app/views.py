from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_api_beginner_app import serializers


class HelloApiView(APIView):
    # Test Api View

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # Returns a list of APIView Features

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        # Create a Hello message with our name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = f'Hello {name}, Your age is {age}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, PK=None):
        # Update the complete object in api
        return Response({'method': 'PUT'})

    def patch(self, request, PK=None):
        # Update the partial part of object in api
        return Response({'method': 'PATCH'})

    def delete(self, request, PK=None):
        # Delete the complete object in api
        return Response({'method': 'DELETE'})