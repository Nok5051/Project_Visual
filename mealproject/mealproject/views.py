import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
# views
from .models import RecipeTable

def index(request):
    return render(request, 'index.html')


def csvLoader(request):
    return HttpResponse('create model <br> upload complete')