
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
    data_lst = []
    context = dict()
    if request.method == 'POST':
        
        gu = request.POST.getlist('gu', ''),
        dong = request.POST.getlist('dong', ''),
        menutype = request.POST.getlist('menutype', ''),
        pricetype = request.POST.getlist('pricetype', '')

        # data_lst.extend({'gu': gu[0]})
        # data_lst.extend({'dong': dong[0]})
        # data_lst.extend({'menutype': menutype[0]})
        # data_lst.extend({'pricetye': pricetype})

        context = {
            'data_lst': {'gu': ''.join(gu[0])}
        }

        print(type(gu[0]), '----------------------')

        print(context)

    return render(request, 'restaurant/map.html', context)

def newstadd(request):

    newadd_lst = []
    st_addr = MapStore.objects.values_list('newstoreadd', flat=True)
    newadd_lst.append(st_addr)

    context = {
        'newadd_lst': newadd_lst
    }

    return render(request, 'restaurant/map.html', context)
