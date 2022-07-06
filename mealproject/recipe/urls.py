from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('getCategory/', views.getCategory),
    path('getMenu/', views.getMenu),
    path('getGraph/', views.getGraph)
]
