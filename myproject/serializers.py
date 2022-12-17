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
