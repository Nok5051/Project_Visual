from rest_framework import serializers
from .models import *

class Map_storeSerializer(serializers.ModelSerializer):
    newstoreadd = models.CharField(db_column='newstoreadd', max_length=100)
    class Meta:
        model = MapStore
        fields = ['newstoreadd']