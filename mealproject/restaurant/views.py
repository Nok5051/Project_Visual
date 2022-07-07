
from django.shortcuts import render, redirect
from django.http import JsonResponse
import pymysql

from .models import MapStore

# pip install djangorestframework
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *



# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html')


# https://devvvyang.tistory.com/37

def getdong(request):
    dong_dict = dict()
    gu_lst = []
    dong_lst = []
    map_addr = MapStore.objects.values_list('addr', flat=True)
    map_list = list(map_addr)

    for i in map_list:
        ms_list = i.split(' ')
        gu_lst.append(ms_list[0])
        ms_dong = []
        ms_dong.append(ms_list[1])
        dong_lst.append(ms_dong)
 
    for i in range(len(gu_lst)):
        if gu_lst[i] not in dong_dict:
            dong_dict[gu_lst[i]] = dong_lst[i]

        else:
            value = dong_dict[gu_lst[i]]
            if dong_lst[i][0] not in value:
                value.extend(dong_lst[i])

    return JsonResponse(dong_dict)


def insert_data(request):
    context = dict()
    if request.method == 'POST':
        gu = request.POST.getlist('gu', '')

        gu1 = request.POST['gu']
        dong1 = request.POST['dong']
        menutype = request.POST['menutype']
        pricetype = request.POST['pricetype']

        result = MapStore.objects.filter(
            addr = gu1+' '+dong1,
            storetype = menutype,
            menu1_price = pricetype
        )

       
        context = {
            'data_lst': {'gu': ''.join(gu[0])},
            'result' : result,
       
        }

    return render(request, 'restaurant/map.html', context)