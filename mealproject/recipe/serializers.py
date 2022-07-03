from rest_framework import serializers
from .models import *

# serializer : 직렬화 - 받아온 데이터를 django에서 처리할 수 있는 데이터형으로 변환

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