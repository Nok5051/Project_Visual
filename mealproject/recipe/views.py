# from django.http import JsonResponse
from django.shortcuts import render
# from django.core import serializers
# from django.http import HttpResponse

# pip install djangorestframework
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# need to draw charts
from plotly.offline import plot
from plotly.graph_objs import Line
import requests
from xml.etree import ElementTree
import pandas as pd


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
    return Response(data=serialized_recipes.data)

def chart(request):
    service_key = 'a934512a-e6a6-475b-963b-f5de5a551889'
    service_id = '2579'

    # 최근 일자 도.소매가격정보(상품 기준)
    url = f'http://www.kamis.or.kr/service/price/xml.do?action=dailyCountyList&p_cert_key={service_key}&p_cert_id={service_id}&p_returntype=xml&p_countycode=1101'
    resp = requests.get(url)
    tree = ElementTree.fromstring(resp.text)

    items = tree[2].findall('item')
    rows = []
    regday = tree[0][0][0].text
    for item in items:
        category_code = item.find('category_code').text
        category_name = item.find('category_name').text
        productno = item.find('productno').text
        productName = item.find('productName').text
        day = item.find('lastest_day').text
        unit = item.find('unit').text
        dpr1 = item.find('dpr1').text
        dpr2 = item.find('dpr2').text
        dpr3 = item.find('dpr3').text
        dpr4 = item.find('dpr4').text

        # 최근 가격추이(상품 기준 - 품목코드)
        url = f'http://www.kamis.or.kr/service/price/xml.do?action=recentlyPriceTrendList&p_productno={productno}&p_regday={day}&p_cert_key={service_key}&p_cert_id={service_id}&p_returntype=xml'
        resp = requests.get(url)
        tree = ElementTree.fromstring(resp.text)
        d10 = tree[2][0].find('d10').text
        d20 = tree[2][0].find('d20').text

        try:
            cost1 = int(dpr1.replace(',', ''))
            cost2 = int(dpr2.replace(',', ''))
            cost3 = int(dpr3.replace(',', ''))
            cost4 = int(dpr4.replace(',', ''))
            cost10 = int(d10.replace(',', ''))
            cost20 = int(d20.replace(',', ''))
        except:
            cost1 = 1
            cost2 = 1
            cost3 = 1
            cost4 = 1
            cost10 = 1
            cost20 = 1

        direction = -1  # 0: 가격하락 / 1: 가격상승 / 2: 등락없음 or 정보없음
        if (cost2 / cost10 == 1):
            direction = 2
        elif (cost2 / cost10 > 1):
            direction = 1
        else:
            direction = 0

        value = 0  # 등락률
        if (direction == 0):
            value = round(cost2 / cost10, 2)
        elif (direction == 1):
            value = round(cost10 / cost2, 2)
        else:
            value = 0

        rows.append({"부류코드": category_code,
                     "부류명": category_name,
                     "품목코드": productno,
                     "품목명": productName,
                     "단위": unit,
                     "당일": cost1,
                     "1일전": cost2,
                     "10일전": cost10,
                     "20일전": cost20,
                     "1개월전": cost3,
                     "1년전": cost4,
                     "등락": direction,
                     "등락률": value
                     })

    ingredient_prices = pd.DataFrame(rows)

    df_graph = ingredient_prices.iloc[0]
    x_data = ['1년전', '1개월전', '20일전', '10일전', '1일전', '당일']
    y_data = [df_graph[10], df_graph[9], df_graph[8], df_graph[7], df_graph[6], df_graph[5]]
    plot_div = plot([Line(x=x_data, y=y_data,)], output_type='div')

    return render(request, 'recipe/index.html', context={'plot_div': plot_div})

