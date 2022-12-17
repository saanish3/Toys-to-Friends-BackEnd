# models.py
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=['organization', 'individual'])

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField()

class Toy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=['available', 'claimed', 'donated'])

# serializers.py
from rest_framework import serializers
from .models import Toy, User, Organization

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

# views.py
from django.shortcuts import render
from rest_framework import generics
from .serializers import ToySerializer, UserSerializer, OrganizationSerializer

class ToyList(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer