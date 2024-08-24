from rest_framework import serializers
from apps.WorldMap import models

class WorldMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorldMap
        fields = ['id','name','capital','subregion','population','region']