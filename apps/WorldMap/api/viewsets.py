from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

# erro ao importar requests, não entendi o motivo.
import requests

from apps.WorldMap.api import serializers
from .serializers import WorldMapSerializer

from apps.WorldMap import models

from apps.WorldMap.models import WorldMap


class worldMapViewSet(ModelViewSet):
    serializer_class = serializers.WorldMapSerializer
    queryset = models.WorldMap.objects.all()

    def create(self, request):
        pais = requests.data.get('name', '')
        
        url = f"https://restcountries.com/v2/name/{pais}"

        requisicao = requests.get(url) 
        json_data = requisicao.json() 


        if isinstance(json_data, list) and json_data:
            country_info = json_data[0] 
            name = country_info.get('name','')
            capital = country_info.get('capital','')
            subregion = country_info.get('subregion','')
            population = country_info.get('population','')
            region = country_info.get('region','')

        dadosrecebidos = { 
            "name": f'{name}',
            "capital": f'{capital}',
            "subregion": f'{subregion}',
            "population": f'{population}',
            "region": f'{region}',
        }
        

        meuserializer = WorldMapSerializer(data=dadosrecebidos)

        if meuserializer.is_valid():
            name_pesquisado = WorldMap.objects.filter(name=name)
            name_pesquisado_existe = name_pesquisado.exists() 

            if name_pesquisado_existe: 
                return Response({"AVISO":"Seu País já existe no bando de dados"})
            
            meuserializer.save() 
            return Response(meuserializer.data)
            
        else:
            return Response({"AVISO: Algo deu errado"})