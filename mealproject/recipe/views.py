# from django.http import JsonResponse
from django.shortcuts import render
# from django.core import serializers
# from django.http import HttpResponse
from .models import *

# pip install djangorestframework
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *



# Create your views here.
def index(request):
    content = {'list': Recipe.objects.all(), 'catogories': Category.objects.all()}
    return render(request, 'recipe/index.html',  content)

@api_view(["GET"])
def getCategory(request):
    catogories = Category.objects.all()
    serialized_categories = CategorySerializer(catogories, many=True)
    return Response(data=serialized_categories.data)

@api_view(["GET"])
def getMenu(request):
    category = request.GET['category']
    recipes = Recipe.objects.filter(category=category)
    serialized_recipes = RecipeSerializer(recipes, many=True)
    print(serialized_recipes)
    return Response(data=serialized_recipes.data)


