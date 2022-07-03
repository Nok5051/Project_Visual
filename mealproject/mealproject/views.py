import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
# views
# from .models import RecipeTable

def index(request):
<<<<<<< HEAD
    return render(request, 'index.html')




=======
    return render(request, 'mealproject/index.html')
>>>>>>> 3737c225b1cefaca8f188674475f7675f72b7e5c
