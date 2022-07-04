from rest_framework import serializers
from .models import *

class Map_storeSerializer(serializers.ModelSerializer):
    category = models.CharField(db_column='MapStore', max_length=100)
    class Meta:
        model = MapStore
        fields = "__all__"