
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

def getgu(request):
    
    gu_list = []
    gu_dict = dict()

    map_addr = MapStore.objects.values_list('addr', flat=True)
    #print(list(map_addr))

    map_list = list(map_addr)
    
    for i in map_list:

        ms_list = i.split(' ')
        if ms_list[0] not in gu_list:
            gu_list.append(ms_list[0])
    
        for y in range(len(gu_list)):
            gu_dict[f'{y}'] = gu_list[y]
    
    return JsonResponse(gu_dict)


def getdong(request):
    dong_list = []
    dong_dict = dict()

    map_addr = MapStore.objects.values_list('addr', flat=True)
    map_list = list(map_addr)

    



    return JsonResponse(dong_dict)





def map_index(request):
    return render(request, 'restaurant/map.html')

