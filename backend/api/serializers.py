from rest_framework import serializers
from .models import Recipe
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ("id", "name", "ingredients", "picture", "difficulty", "prep_time", "cook_time", "guide")

class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'first_name', 'last_name')