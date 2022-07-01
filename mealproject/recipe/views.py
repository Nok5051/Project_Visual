from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    content = {'list': Recipe.objects.all(), 'catogories': Category.objects.all()}
    return render(request, 'recipe/index.html',  content)

# def category(request, category):
#     category_filter = Recipe.objects.filter(category=category)
#     category_dict = {"mainside": "메인반찬", "noodle":"면/만두", "soup":"국/탕", "stew":"찌개", "western":"양식", "fusion":"퓨전", "":"" }
#     print("hello",category_dict["category"])
#     return render(request, f'recipe/{category}.html', {'list': category_filter})

def category(request):
    category_filter = Recipe.objects.filter(category="메인반찬")
    print("hello")
    return render(request, 'recipe/maindish.html', {'list': category_filter})
