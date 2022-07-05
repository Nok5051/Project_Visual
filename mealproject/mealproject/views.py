import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
# views
# from .models import RecipeTable

def index(request):
    return render(request, 'mealproject/index.html')
<<<<<<< HEAD

=======
>>>>>>> de1c1f2de59157a0399bcf1f60407f1d4b34e4af
