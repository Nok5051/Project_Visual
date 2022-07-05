
from django.shortcuts import render
from django.http import JsonResponse

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
    
    dong_list = []
    dong_dict = dict()

    map_addr = MapStore.objects.values_list('addr', flat=True)
    
    map_list = list(map_addr)

    for i in map_list:
        ms_list = i.split(' ')

        dong_dict['gu'] = ms_list[0]
        dong_dict['dong'] = ms_list[1]
        
        if dong_dict not in dong_list:
            dong_list.append(dong_dict)
        print(ms_list)


    print(dong_lst)


    return JsonResponse(dong_dict)


def map_index(request):
    return render(request, 'restaurant/map.html')

