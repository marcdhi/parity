from django.shortcuts import render
from rest_framework import generics 
from .serializers import RoomSerializer

# Importing the Room model
from .models import Room

class RoomView(generics.ListCreateAPIView):
    # Specifying the serializer class
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

