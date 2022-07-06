from django.shortcuts import render
from django.core import serializers
from .models import *

# pip install djangorestframework
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


import pandas as pd
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    ingredient_price = pd.read_csv('C:/workspaces/workspace_project/Project_Visual/recipe_data/data_for_graph.csv')
    df_down = ingredient_price[ingredient_price['등락'] == 0].sort_values(by='등락률', ascending=False)
    df_up = ingredient_price[ingredient_price['등락'] == 1].sort_values(by='등락률', ascending=False)
    index_down1 = df_down.iloc[0, 3]
    index_down2 = df_down.iloc[1, 3]
    index_down3 = df_down.iloc[2, 3]
    index_up1 = df_up.iloc[0, 3]
    index_up2 = df_up.iloc[1, 3]
    index_up3 = df_up.iloc[2, 3]
    down1 = [df_down.iloc[0, 10], df_down.iloc[0, 9], df_down.iloc[0, 8], df_down.iloc[0, 7], df_down.iloc[0, 6], df_down.iloc[0, 5]]
    down2 = [df_down.iloc[1, 10], df_down.iloc[1, 9], df_down.iloc[1, 8], df_down.iloc[1, 7], df_down.iloc[1, 6], df_down.iloc[1, 5]]
    down3 = [df_down.iloc[2, 10], df_down.iloc[2, 9], df_down.iloc[2, 8], df_down.iloc[2, 7], df_down.iloc[2, 6], df_down.iloc[2, 5]]
    up1 = [df_up.iloc[0, 10], df_up.iloc[0, 9], df_up.iloc[0, 8], df_up.iloc[0, 7], df_up.iloc[0, 6], df_up.iloc[0, 5]]
    up2 = [df_up.iloc[1, 10], df_up.iloc[1, 9], df_up.iloc[1, 8], df_up.iloc[1, 7], df_up.iloc[1, 6], df_up.iloc[1, 5]]
    up3 = [df_up.iloc[2, 10], df_up.iloc[2, 9], df_up.iloc[2, 8], df_up.iloc[2, 7], df_up.iloc[2, 6], df_up.iloc[2, 5]]

    content = {'list': Recipe.objects.all(), 'catogories': Category.objects.all(),'index_down1':index_down1, 'index_down2':index_down2, 'index_down3':index_down3, 'index_up1':index_up1, 'index_up2':index_up2, 'index_up3':index_up3, 'down1':down1, 'down2':down2, 'down3':down3, 'up1':up1, 'up2':up2, 'up3':up3}
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
    return Response(data=serialized_recipes.data)

@api_view(["GET"])
def getGraph(request):
    ingredient = request.GET['ingredient']
    ingredient_price = pd.read_csv('./recipe_data/data_for_graph.csv')
    df_graph = ingredient_price[ingredient_price['품목명'] == ingredient]
    data = json.dumps({'value' : [int(df_graph.iloc[0,10]), int(df_graph.iloc[0,9]), int(df_graph.iloc[0,8]), int(df_graph.iloc[0,7]), int(df_graph.iloc[0,6]), int(df_graph.iloc[0,5])]})

    return HttpResponse(data, content_type="application/json")

