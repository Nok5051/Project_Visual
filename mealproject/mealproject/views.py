import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
# views
from .models import RecipeTable

def index(request):
<<<<<<< HEAD
    return render(request, 'index.html')


def csvLoader(request):
    return HttpResponse('create model <br> upload complete')
=======
    return render(request, 'mealproject/index.html')
>>>>>>> da601e10bb8ae4a873ee02e3d95c613bc64bf635
