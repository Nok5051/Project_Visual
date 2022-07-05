from django.urls import path
from . import views


urlpatterns = {
    path('', views.index),
    path('getgu/', views.getgu),
    path('map_index/', views.map_index, name='mappage'),
    
}