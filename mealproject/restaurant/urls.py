from django.urls import path
from . import views


urlpatterns = {
    path('', views.index),
    path('getgugun/', views.getgugun),
    path('map_index/', views.map_index, name='mappage'),
    
}