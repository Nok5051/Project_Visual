from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('getdong/', views.getdong),
    path('mappage/', views.insert_data, name='mappage'),
    path('storeadd/', views.newstadd, name='nst'),


]