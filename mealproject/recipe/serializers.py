from rest_framework import serializers
from .models import *

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('category')

class CategorySerializer(serializers.ModelSerializer):
    category = models.CharField(db_column='CATEGORY', max_length=10)
    class Meta:
        model = Category
        fields = "__all__"

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"