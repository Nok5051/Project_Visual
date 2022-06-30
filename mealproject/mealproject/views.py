from django.shortcuts import render

def index(request):
    return render(request, 'mealproject/index.html')
