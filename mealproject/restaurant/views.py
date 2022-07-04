
from django.shortcuts import render

# pip install djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *



# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html')


# https://devvvyang.tistory.com/37

def getgugun(request):
    
    gugun = dict()

    map_store = Map_store.objects.values_list('addr')

    ms_list = map_store.values().str.split(' ')
    gugun['gu'] = ms_list.str.get(0)
    gugun['dong'] = ms_list.str.get(1)

    print(ms_list)

    serialized_gugun = CategorySerializer(gugun, many=True)
    return Response(data=serialized_gugun.data)




def map_index(request):
    return render(request, 'restaurant/map.html')

