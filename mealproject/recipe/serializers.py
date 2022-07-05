from rest_framework import serializers
from .models import *

# serializer : 직렬화 - 받아온 데이터를 django에서 처리할 수 있는 데이터형으로 변환

class CategorySerializer(serializers.ModelSerializer):
    category = models.CharField(db_column='CATEGORY', max_length=10)
    class Meta:
        model = Category
        fields = "__all__"

class RecipeSerializer(serializers.ModelSerializer):
    unit_price = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('recipe_nm', 'qnt', 'recipe', 'ingredients', 'units', 'total_price', 'unit_price')

    def get_unit_price(self, obj):
        return round(int(obj.total_price) / int(obj.qnt[0]))